from fastapi import HTTPException, status, APIRouter, Depends, Request, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from services.sellers import become_a_seller, get_shop_details
from services.products import get_products_by_seller
from dependencies.database import get_db
from dependencies.auth import current_user
from schemas.sellers import SellerCreate
from schemas.product import ProductFullCreate, ProductFullUpdate, VariantUpdate
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


@router.get("/shop", status_code=status.HTTP_200_OK)
async def get_seller_shop(
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(current_user)
):
    if not current_user and not current_user.is_seller:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only sellers can access their shop."
        )
    
    return await get_shop_details(db, current_user.id)


@router.get("/my-products", status_code=status.HTTP_200_OK)
async def get_my_products(
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(current_user)
):
    if not current_user or not current_user.is_seller:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only sellers can access their products."
        )
    
    products = await get_products_by_seller(db, current_user.id)
    return products

