from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, EmailStr, ValidationError  # type: ignore
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas.user import UserCreate, UserOut
from models.user import User


def insert_user(db: Session, user_data: dict):
    try:
        user = UserCreate(**user_data)
        if db.query(User).filter(User.email == user.email).first():
            print(f"User with email {user.email} already exists")

        new_user = User(name=user.name, email=user.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print("Inserted user: ", UserOut.model_validate(new_user))
    except ValidationError as e:
        print("Validation error: ", e)


def fetch_users(db: Session) -> List[UserOut]:
    users = db.query(User).all()
    return [UserOut.model_validate(user) for user in users]


def filter_users_by_email(db: Session, email: str) -> Optional[UserOut]:
    user = db.query(User).filter(User.email == email).first()
    if user:
        return UserOut.model_validate(user)
    return None


def insert_many_users(db: Session, user_data_list: list[UserCreate]):
    try:
        for user_data in user_data_list:
            user = User(name=user_data.name, email=user_data.email)
            db.add(user)
        return {"status": "success", "message": "Users inserted."}
    except IntegrityError as e:
        db.rollback()
        return {"status": "error", "message": f"Failed to insert: {str(e.orig)}"}
