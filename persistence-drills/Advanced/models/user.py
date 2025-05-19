from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base  # SQLAlchemy declarative base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # One-to-many: a user can have many posts
    posts = relationship("Post", back_populates="owner",
                         cascade="all, delete-orphan")
