from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash, verify_password
from typing import Optional

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).get(user_id)

def create_user(db: Session, *, email: str, password: str) -> User:
    hashed = get_password_hash(password)
    db_user = User(email=email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
