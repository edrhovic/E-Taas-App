from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, foreign_key="categories.id")
    user_id = Column(Integer, foreign_key="users.id")
    product_name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    category = relationship("Category", back_populates="products")
    user = relationship("User", back_populates="products")

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"