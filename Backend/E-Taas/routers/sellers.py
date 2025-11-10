from fastapi import HTTPException, status, APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from services.sellers import become_a_seller
from dependencies.database import get_db
from dependencies.auth import current_user
from schemas.sellers import SellerCreate
import logging
from dependencies.limiter import limiter
from models.users import User

router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/apply", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def apply_as_seller(
    request: Request,
    seller_data: SellerCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(current_user)
):
    """Endpoint for users to apply as sellers."""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required to apply as a seller."
        )
    if current_user.is_seller:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already a seller."
        )
    
    
    return await become_a_seller(db, seller_data, current_user.id)
