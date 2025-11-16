from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    product_name: str
    description: Optional[str] = None
    base_price: float
    stock: int
    has_variants: bool = False
    category_id: int

class ProductCreate(ProductBase):
    seller_id: int

class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    description: Optional[str] = None
    base_price: Optional[float] = None
    stock: Optional[int] = None
    has_variants: Optional[bool] = None
    category_id: Optional[int] = None

