from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .products import ProductResponse

class OrderDetailResponse(BaseModel):
    id: int
    product: ProductResponse
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    order_details: List[OrderDetailResponse]

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    delivery_address: str

