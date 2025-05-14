from pydantic import BaseModel
from typing import List
from schemas.post import PostOut
from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    id: int
    name: str
    email: str

    model_config = {
        "from_attributes": True
    }


class UserWithPosts(UserOut):
    posts: List[PostOut] = []


class UserCreate(BaseModel):
    name: str
    email: EmailStr
