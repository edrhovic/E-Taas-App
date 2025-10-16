from models import User
from core.security import hash_password, create_access_token, verify_password
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from schemas.auth import LoginBase
from core.config import settings
from sqlalchemy import or_

def register_user(user: UserCreate, db: Session):
    db_user = db.query(User).filter(
        or_(User.username == user.username, User.email == user.email)
    ).first()
    if db_user:
        return None, "Username or email already registered"

    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=False,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user, None


def login_user(user: LoginBase, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        return None, "Invalid email or password"
    
    if not verify_password(user.password, db_user.hashed_password):
        return None, "Invalid email or password"
    
    expires_delta = timedelta(days=7) if getattr(user, "remember_me", False) else timedelta(hours=1)
    expires = datetime.utcnow() + expires_delta
    access_token = create_access_token(
        data={
        "sub": db_user.email,
        "user_id": db_user.id,
        "role": db_user.role,
        "exp": expires
    },
        secret_key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": int(expires_delta.total_seconds())
    }, None


