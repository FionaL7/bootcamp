from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.post import Post
from models.user import User
from database import engine, SessionLocal, Base
from schemas.post import PostOut, UserWithPosts, PostCreate
from schemas.user import UserCreate
from crud.post import get_user_with_posts, create_post
from crud.user import insert_user, filter_users_by_email, insert_many_users

Base.metadata.create_all(bind=engine)
# Post.Base.metadata.create_all(bind=engine)

db: Session = SessionLocal()

user = filter_users_by_email(db, "ellis@example.com")
# if not user:
#     user = insert_user(db, {"name": "Ellis", "email": "ellis@example.com"})
# print(user)
# post_data = PostCreate(title="First Post", content="This is Alice's post")
# create_post(db, post_data, user_id=user.id)


# user_with_posts = get_user_with_posts(db, user.email)
# print(UserWithPosts.model_validate(user_with_posts).model_dump())

user_list = [
    UserCreate(name="Elliot", email="elliot@example.com"),
    UserCreate(name="Pam", email="pam@example.com"),
    UserCreate(name="Eve", email="eve@example.com")
]

many_users = insert_many_users(db, user_list)
print(many_users)
db.close()
