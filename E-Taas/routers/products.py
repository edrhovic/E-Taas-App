from services.products import create_product, update_product, delete_product, get_all_product, get_product_by_id
from models.products import Product
from models.users import User
from fastapi import APIRouter, HTTPException, Depends
from db.database import get_db
from core.config import settings
from sqlalchemy.orm import Session
from schemas.products import ProductCreate, ProductResponse, ProductUpdate
from dependencies.auth import current_user


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def get_all_products(db: Session = Depends(get_db), user: User = Depends(current_user)):
    if not user:
        raise HTTPException(404, "User not found")
    
    return get_all_product(db = db)

@router.get("/{id}")
def get_product_with_id(product_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    if not user:
        raise HTTPException(404, "User not found")
    return get_product_by_id(product_id=product_id, db=db)

@router.post("/add", response_model = ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):

    if user.role != "seller":
        raise HTTPException(status_code=403, detail="Only sellers can add products")
    
    product_data = {
        "product_name": product.product_name,
        "price": product.price,
        "description": product.description,
        "stock": product.stock,
        "image_url": product.image_url,
        "category_id": product.category_id,
        "seller_id": user.id, 
    }

    return create_product(product=product_data, db=db)

@router.post("/update", response_model=ProductResponse)
def product_update(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if user.role != "seller":
        raise HTTPException(status_code=403, detail="Only sellers can update products")
    
    if product.seller_id != user.id:
        raise HTTPException(status_code=403, detail="You can only update your own products")
    
    update_product_data = product_update.dict(exclude_unset=True)

    updated_product = update_product(product_id, update_product_data, db)
    return updated_product

@router.post("/delete/{id}")
def product_delete(product_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    if user.role != "seller":
        raise HTTPException(status_code=403, detail="Only sellers can delete products")
    
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return delete_product(product_id=product_id, db=db)
    
