from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, EmailStr, ValidationError  # type: ignore
from database import Base, engine, SessionLocal
from typing import List, Optional
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


def filter_users_by_email(db: Session, email: str) -> Optional[UserSchema]:
    user = db.query(User).filter(User.email == email).first()
    if user:
        return UserSchema.model_validate(user)
    return None


def update_email(db: Session, old_email: str, new_email: str) -> str:
    user = db.query(User).filter(User.email == old_email).first()
    if not user:
        return f"No user with '{old_email}' found."

    if db.query(User).filter(User.email == new_email).first():
        return f"Email already in use"

    user.email = new_email
    db.commit()
    db.refresh(user)
    return f"Email updated successfully!"


def delete_user(db: Session, name: str) -> str:
    user = db.query(User).filter(User.name == name).first()

    if not user:
        return f"User not found"

    db.delete(user)
    db.commit()

    return f"User {name} has been deleted"


if __name__ == "__main__":
    db = SessionLocal()
    # insert_user(db, {"name": "Fiona", "email": "fiona@email.com"})
    # insert_user(db, {"name": "Charlie", "email": "charlie@example.com"})

    # print("\n📥 Fetching user by email:")
    # user_email = filter_users_by_email(db, "charlie@example.com")
    # print(user_email if user_email else "User not found")

    # email_updation = update_email(db, "fiona@email.com", "fiona7@email.com")
    # print(email_updation)
    print("\n Deleting user:")
    msg = delete_user(db, "Fiona")
    print(msg)
    all_users = fetch_users(db)
    for user in all_users:
        print(user)
