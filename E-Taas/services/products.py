from models import Product
from sqlalchemy.orm import Session
from datetime import datetime
from schemas.products import ProductCreate, ProductUpdate

def create_product(product: dict, db: Session):
    new_product = Product(
        product_name=product["product_name"],
        price=product["price"],
        description=product.get("description"),
        stock=product.get("stock", 0),
        image_url=product.get("image_url"),
        category_id=product["category_id"],
        seller_id=product["seller_id"], 
        created_at=datetime.utcnow()
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all_product(db: Session, limit = 100):
    return db.query(Product).limit(limit=limit).all()


def get_product_by_id(product_id: int, db: Session):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(product_id: int, update_product: dict, db: Session):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None
    for key, value in update_product.items():
        setattr(product, key, value)
    product.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(product)
    return product

def delete_product(product_id: int, db: Session):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None
        db.delete(product)
        db.commit()
        return {"Success": "Deletion of account successful"}
    except:
        return {"Error", "Something went wrong on deletion"}
    
