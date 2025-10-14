from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    hashed_password = Column(String)
    role = Column(String)
    brith_date = Column(DateTime, nullable=True)
    age = Column(Integer, nullable=True)
    address = Column(String)
    contact_number = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    product = relationship("Product", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, role={self.role})>"

