from sqlalchemy import select
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from models.sellers import Seller
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sellers import SellerCreate
import logging

logger = logging.getLogger(__name__)

async def become_a_seller(db: AsyncSession, seller_data: SellerCreate, user_id: int) -> Seller:
    try:
        seller = await db.execute(select(Seller).where(Seller.user_id == user_id))
        existing_seller = seller.scalar_one_or_none()
        if existing_seller:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User is already a seller."
            )
        
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required to apply as a seller."
            )

        new_seller = Seller(
            user_id=user_id,
            business_name=seller_data.business_name,
            business_address=seller_data.business_address,
            business_contact=seller_data.business_contact,
            display_name=seller_data.display_name,
            owner_address=seller_data.owner_address
        )
        
        db.add(new_seller)
        await db.commit()
        await db.refresh(new_seller)


        return JSONResponse(
            status_code = status.HTTP_201_CREATED,
            content={
                "message": "Seller application successful",
                "seller_id": new_seller.id,
                "is_verified": new_seller.is_verified
            }
        )

    except HTTPException:
        raise

    except Exception as e:
        logger.error(f"Error in become_a_seller: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )