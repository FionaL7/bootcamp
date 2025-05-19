from sqlalchemy.orm import Session
from models.post import Post
from schemas.post import PostCreate
from models.user import User
from schemas.post import UserWithPosts


def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_user_with_posts(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return f"❌ User '{email}' not found."

    return UserWithPosts.model_validate(user)
