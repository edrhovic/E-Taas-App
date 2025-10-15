from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.orders import OrderResponse, OrderCreate
from services import orders as order_service
from db.database import get_db
from dependencies.auth import current_user
from models.users import User
from models.orders import Order

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def place_order(order_data: OrderCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    
    return order_service.create_order_from_cart(db, user.id, order_data.delivery_address)

@router.get("/", response_model=List[OrderResponse])
def get_user_orders(db: Session = Depends(get_db), user: User = Depends(current_user)):
    
    orders = db.query(Order).filter(Order.user_id == user.id).all()
    return orders

