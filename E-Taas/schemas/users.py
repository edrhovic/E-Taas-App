from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[str] = None
    birth_date: Optional[datetime] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None

    #if user became a seller
    store_name: Optional[str] = None
    store_description: Optional[str] = None
    rating: Optional[float] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime]
    role: str
    is_active: bool
    store_name: Optional[str] 
    store_description: Optional[str] 
    rating: Optional[float] 
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True