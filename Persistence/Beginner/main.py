from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, EmailStr, ValidationError  # type: ignore
from database import Base, engine, SessionLocal
from typing import List
from sqlalchemy.orm import Session


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


Base.metadata.create_all(bind=engine)


class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserOutput(BaseModel):
    id: int
    name: str
    email: EmailStr
    model_config = {
        "from_attributes": True
    }


def insert_user(db: Session, user_data: dict):
    try:
        user = UserCreate(**user_data)
        if db.query(User).filter(User.email == user.email).first():
            print(f"User with email {user.email} already exists")

        new_user = User(name=user.name, email=user.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print("Inserted user: ", UserSchema.model_validate(new_user))
    except ValidationError as e:
        print("Validation error: ", e)


def fetch_users(db: Session) -> List[UserSchema]:
    users = db.query(User).all()
    return [UserSchema.model_validate(user) for user in users]


if __name__ == "__main__":
    db = SessionLocal()
    insert_user(db, {"name": "Fiona", "email": "fiona@email.com"})

    all_users = fetch_users(db)
    for user in all_users:
        print(user)
