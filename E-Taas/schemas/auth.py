from pydantic import BaseModel, EmailStr
from typing import Optional


class LoginBase(BaseModel):
    email: EmailStr
    password: str
    remember_me: bool


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int