from sqlalchemy.orm import Session
from models.cart import Cart
from models.orders import Order
from models.order_details import OrderDetails
from models.products import Product
from fastapi import HTTPException, status
from models import CartItem
from datetime import datetime

def create_order_from_cart(db: Session, user_id: int, delivery_address: str) -> Order:
    
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    if not cart or not cart.items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart is empty")

    total_amount = 0
    order_details_list = []

    for item in cart.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product or product.stock < item.quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product '{product.product_name}' is out of stock or not available in the desired quantity.")
        
        total_price_for_item = product.price * item.quantity
        total_amount += total_price_for_item
        
        order_detail = OrderDetails(
            product_id=item.product_id,
            user_id=user_id,
            quantity=item.quantity,
            price=product.price,
            total_price=total_price_for_item,
            delivery_address=delivery_address
        )
        order_details_list.append(order_detail)
        product.stock -= item.quantity

    new_order = Order(user_id=user_id, total_amount=total_amount, status="pending")
    db.add(new_order)
    db.flush()

    for detail in order_details_list:
        detail.order_id = new_order.id
        db.add(detail)

    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete()
    db.commit()
    db.refresh(new_order)
    return new_order

