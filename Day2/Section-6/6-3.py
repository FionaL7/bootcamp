from pydantic import BaseModel, Field
# 1. Field Descriptions


class User(BaseModel):
    email: str = Field(..., description="User's email address")


# 2. Field Aliases

class User(BaseModel):
    id: int = Field(..., alias="user_id")


# Accepts JSON like {"user_id": 123}
data = {"user_id": 123}
user = User(**data)
print(user.id)

# 3. Title and Examples


class User(BaseModel):
    username: str = Field(..., title="Username", example="FiFi123")
    age: int = Field(..., title="User Age", example=21)

# 4. Model Docstrings


class User(BaseModel):
    """
    This model represents a user profile including identity and access data.
    """

    name: str
    email: str
