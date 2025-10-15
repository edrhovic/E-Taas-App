
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from db.database import Base

class OrderDetails(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    quantity = Column(Integer)
    order_status = Column(String, default="pending")
    delivery_address = Column(String)
    price = Column(Float)
    total_price = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="order_details")
    user = relationship("User", back_populates="order_details")
