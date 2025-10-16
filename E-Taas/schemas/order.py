from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderCreate(BaseModel):
    selected_items: list[int]
    delivery_address: str
    payment_method: str
    contact_number: str

class OrderDetailSchema(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    total_price: float

    class Config:
        orm_mode = True

class OrderSchema(BaseModel):
    id: int
    user_id: int
    total_amount: float
    order_status: str
    delivery_address: str
    payment_method: str
    contact_number: str
    created_at: datetime
    details: List[OrderDetailSchema]

    class Config:
        orm_mode = True