from collections import namedtuple
from dataclasses import dataclass

# Basic Dataclass


@dataclass
class User:
    name: str
    age: int


u1 = User("alex", 23)
print(u1)

#  Default Values


@dataclass
class User:
    name: str
    age: int = 0


u2 = User("Tiny alex")
print(u2)

# Frozen Dataclass


@dataclass(frozen=True)
class FrozenUser:
    name: str
    age: int


fu = FrozenUser("Ice Queen", 99)

# Comparison Support
u3 = User("alex", 23)
u4 = User("alex", 23)
print(u3 == u4)

# Custom Method in Dataclass


@dataclass
class User:
    name: str
    age: int = 0

    def is_adult(self):
        return self.age >= 18


print(User("alex", 23).is_adult())  # True
print(User("Baby alex").is_adult())  # False

# NamedTuple Basics
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2

# Field Rename with Invalid Inputs
Point = namedtuple('Point', ['x', 'y', '1invalid'], rename=True)
p = Point(1, 2, 3)


@dataclass
class AdminUser(User):
    permissions: list


admin = AdminUser("alex the Great", 23, permissions=["ban", "delete"])
# AdminUser(name='alex the Great', age=23, permissions=['ban', 'delete'])
print(admin)
print(p)  # Point(x=1, y=2, _2=3)
