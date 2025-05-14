from pydantic import BaseModel


class PostOut(BaseModel):
    id: int
    title: str
    content: str

    model_config = {
        "from_attributes": True
    }


class PostCreate(BaseModel):
    title: str
    content: str


class UserWithPosts(BaseModel):
    id: int
    name: str
    email: str
    posts: list[PostOut] = []

    model_config = {
        "from_attributes": True
    }
