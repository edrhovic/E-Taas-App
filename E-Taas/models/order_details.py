from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class OrderDetails(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    quantity = Column(Integer)
    order_status = Column(String)
    delivery_address = Column(String)
    price = Column(Float)
    total_price = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    product = relationship("Product", back_populates="order_details")
    user = relationship("User", back_populates="order_details")
    seller = relationship("Seller", back_populates="order_details")

    def __repr__(self):
        return f"<OrderDetails(order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity}, total_price={self.total_price})>"