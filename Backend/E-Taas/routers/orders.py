from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.orders import OrderCreate
from models.orders import Order
from services.orders import get_orders_by_user, create_new_order
from dependencies.auth import current_user
from dependencies.database import get_db
from dependencies.limiter import limiter

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
@limiter.limit("10/minute")
async def get_user_orders(
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(current_user)
):
    orders = await get_orders_by_user(db, current_user.id)
    return orders

@router.post("/", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def create_order(
    request: Request,
    order: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(current_user)
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required to create an order."
        )
    
    new_order = await create_new_order(db, order, current_user.id)
    return new_order