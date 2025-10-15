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
    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    role: str
    is_active: bool
    created_at: Optional[datetime]

    class Config:
        orm_mode = True