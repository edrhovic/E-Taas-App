from pydantic import BaseModel
from typing import List, Optional

class OrderItemBase(BaseModel):
    product_id: int
    variant_id: Optional[int] = None
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderBase(BaseModel):
    shipping_address: str
    payment_method: str
    items: List[OrderItemCreate]

class OrderCreate(OrderBase):
    seller_id: int

class OrderBaseCart(BaseModel):
    shipping_address: str
    payment_method: str

class OrderCreateCart(OrderBaseCart):
    seller_id: int
    cart_item_id: Optional[int] = None
    

class OrderItemResponse(BaseModel):
    product_id: int
    variant_id: Optional[int] = None
    quantity: int
    price: float

class OrderItemResponse(BaseModel):
    product_id: int
    variant_id: Optional[int] = None
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    seller_id: int
    total_amount: float
    shipping_address: str
    shipping_fee: float
    payment_method: str
    order_reference: str
    shipping_link: Optional[str] = None
    status: str
    payment_status: str
    created_at: str
    shipped_at: Optional[str] = None
    order_received_at: Optional[str] = None
    items: List[OrderItemResponse]

    class Config:
        orm_mode = True