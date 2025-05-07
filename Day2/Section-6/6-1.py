from dataclasses import dataclass, field
from typing import List
# Basic Dataclass


@dataclass
class User:
    name: str
    age: int

# Add Default Value


@dataclass
class User:
    name: str
    age: int
    country: str = "India"

# Post-Init Validation


@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

# Frozen Dataclass (Immutable)


@dataclass(frozen=True)
class FrozenUser:
    name: str
    age: int

# Custom Method: is_adult()


@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def is_adult(self) -> bool:
        return self.age >= 18
# Factory Default for Lists


@dataclass
class User:
    name: str
    age: int
    tags: List[str] = field(default_factory=list)


# Comparison Support
user1 = User("Fi", 25)
user2 = User("Fi", 25)

print(user1 == user2)  # ✅ True because dataclass auto-implements __eq__

# Dataclass with Slots (Space-Saving)


@dataclass(slots=True)
class SlimUser:
    name: str
    age: int
