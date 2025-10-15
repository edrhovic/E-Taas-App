from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductCreate(BaseModel):
    product_name: str
    price: float
    description: Optional[str] = None
    stock: int = 0
    image_url: Optional[str] = None
    category_id: int

class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    stock: Optional[int] = None
    image_url: Optional[str] = None
    category_id: Optional[int] = None

class ProductResponse(BaseModel):
    id: int
    product_name: str
    price: float
    description: Optional[str]
    stock: int
    image_url: Optional[str]
    category_id: int
    seller_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True