from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.database import Base

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    store_name = Column(String, unique=True, index=True)
    store_description = Column(String, nullable=True)
    rating = Column(Float, default=0.0)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="seller")
    products = relationship("Product", back_populates="seller")
    order_details = relationship("OrderDetails", back_populates="seller")

    def __repr__(self):
        return f"<Seller(store_name={self.store_name}, rating={self.rating})>"
