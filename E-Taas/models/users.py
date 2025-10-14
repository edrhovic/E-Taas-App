from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")
    birth_date = Column(DateTime, nullable=True)
    age = Column(Integer, nullable=True)
    address = Column(String, nullable=True)
    contact_number = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    products = relationship("Product", back_populates="user")
    order_details = relationship("OrderDetails", back_populates="user")
    seller = relationship("Seller", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, role={self.role})>"
