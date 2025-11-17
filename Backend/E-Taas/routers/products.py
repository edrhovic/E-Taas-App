from fastapi import HTTPException, status, APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from services.products import get_product_by_id, get_all_products
from dependencies.database import get_db
from dependencies.auth import current_user
from dependencies.limiter import limiter

router = APIRouter()

@router.get("/products")
@limiter.limit("20/minute")
async def get_products(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    
  return await get_all_products(db)

@router.get("/products/{product_id}")
@limiter.limit("30/minute")
async def get_product(
    request: Request,
    product_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await get_product_by_id(db, product_id)