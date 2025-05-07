from pydantic import BaseModel, ValidationError,  conint, constr, validator
from typing import Optiona
# 1. Basic Model


class User(BaseModel):
    name: str
    age: int


data = {"name": "Alice", "age": 30}
user = User(**data)
print(user)

# 2. Validation Error
try:
    bad_data = {"name": "Bob", "age": "not a number"}
    user = User(**bad_data)
except ValidationError as e:
    print(e)

# 3. Nested Models


class Profile(BaseModel):
    bio: str
    location: str


class User(BaseModel):
    name: str
    age: int
    profile: Profile


nested_data = {
    "name": "Fiona",
    "age": 25,
    "profile": {
        "bio": "Coder by night 🌙",
        "location": "Earth"
    }
}
user = User(**nested_data)
print(user)

# 4. Field Constraints


class User(BaseModel):
    username: constr(min_length=3)
    age: conint(gt=0)


user = User(username="Fiona", age=20)
print(user)

# 5. Custom Validaton


class User(BaseModel):
    name: str
    age: int

    @validator("name")
    def name_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError("name must be capitalized")
        return v


 # 6. Automatic Conversion
# string will be converted to int automatically
user = User(name="Fi", age="42")
print(user)

# 7. Export to Dict/JSON
print(user.dict())
print(user.json())

# 8. Optional Field with Default


class User(BaseModel):
    name: str
    age: int
    nickname: Optional[str] = None


u = User(name="Fi", age=25)
print(u.nickname)  # None by default
