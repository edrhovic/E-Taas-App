from sqlalchemy.orm import Session
from models import User
from datetime import datetime


def get_user_details(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def update_user_details(user_id: int, update_data: dict, db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None
    
    for key, value in update_data.items():
        setattr(user, key, value)

    user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user

def delete_user_account(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return {"Success": "Account deletion successful"}

