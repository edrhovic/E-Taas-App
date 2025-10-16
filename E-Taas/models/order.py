from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, func
from db.database import Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Float)
    order_status = Column(String, default="pending")
    delivery_address = Column(String)
    payment_method = Column(String)
    contact_number = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="orders")
    details = relationship("OrderDetail", back_populates="order")