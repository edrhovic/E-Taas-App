from fastapi import APIRouter, Depends, status, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from dependencies.database import get_db
from dependencies.auth import current_user
from services.admin import add_new_category, add_service_category, approve_seller
from services.auth import create_admin_user
from schemas.auth import AdminRegister
from models.users import User
from dependencies.limiter import limiter

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

@router.post("/register-admin", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def register_admin(
    request: Request,
    admin_data: AdminRegister,
    db: AsyncSession = Depends(get_db),
):
    """Register a new admin. Only run once by the deverloper."""
    return await create_admin_user(db, admin_data)
  

@router.post("/add-product-category", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def create_category(
    request: Request,
    category_name: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(current_user)
):
    """Add a new product category. Admin only."""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform this action"
        )
    return await add_new_category(db, category_name)

@router.post("/add-service-category", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def create_service_category(
    request: Request,
    category_name: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(current_user)
):
    """Add a new service category. Admin only."""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform this action"
        )
    return await add_service_category(db, category_name)

@router.put("/verify-seller", status_code=status.HTTP_200_OK)
@limiter.limit("5/minute")
async def verify_seller(
    request: Request,
    seller_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(current_user)
):
    """Approve a seller. Admin only."""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform this action"
        )
    return await approve_seller(db, seller_id)