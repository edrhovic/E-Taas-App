from pydantic import BaseModel
from typing import Optional, List

class ProductBase(BaseModel):
    product_name: str
    description: Optional[str] = None
    base_price: float
    stock: int
    has_variants: bool = False
    category_id: int

class ProductCreate(ProductBase):
    seller_id: int


class VariantBase(BaseModel):
    stock: Optional[int] = 0
    price: Optional[float] = 0.0
    image_url: Optional[str] = None


class VariantCreate(VariantBase):
    pass


class VariantAttributeCreate(BaseModel):
    value: Optional[str] = None

class VariantCategoryCreate(BaseModel):
    category_name: Optional[str] = None
    attributes: Optional[List[VariantAttributeCreate]] = None


class ProductFullCreate(BaseModel):
    product: ProductCreate
    variant_categories: Optional[List[VariantCategoryCreate]] = None
    variants: Optional[List[VariantCreate]] = None
