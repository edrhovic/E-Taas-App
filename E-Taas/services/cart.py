from sqlalchemy.orm import Session
from models.cart import Cart, CartItem
from models.products import Product
from fastapi import HTTPException, status

def get_or_create_cart(db: Session, user_id: int) -> Cart:
   
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart

def add_item_to_cart(db: Session, user_id: int, product_id: int, quantity: int) -> Cart:
    
    cart = get_or_create_cart(db, user_id)
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    if product.stock < quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough stock")

    cart_item = db.query(CartItem).filter(CartItem.cart_id == cart.id, CartItem.product_id == product_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.add(cart_item)
    
    db.commit()
    db.refresh(cart)
    return cart

def remove_item_from_cart(db: Session, user_id: int, product_id: int) -> Cart:
    
    cart = get_or_create_cart(db, user_id)
    cart_item = db.query(CartItem).filter(CartItem.cart_id == cart.id, CartItem.product_id == product_id).first()

    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not in cart")

    db.delete(cart_item)
    db.commit()
    db.refresh(cart)
    return cart

def update_cart_item_quantity(db: Session, user_id: int, product_id: int, quantity: int) -> Cart:
    
    if quantity <= 0:
        return remove_item_from_cart(db, user_id, product_id)
        
    cart = get_or_create_cart(db, user_id)
    cart_item = db.query(CartItem).filter(CartItem.cart_id == cart.id, CartItem.product_id == product_id).first()

    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not in cart")

    cart_item.quantity = quantity
    db.commit()
    db.refresh(cart)
    return cart

