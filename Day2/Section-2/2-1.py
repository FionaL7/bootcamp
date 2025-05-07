import os

# EAFP Basics: Accessing a key with try/except
d = {"name": "Fiona"}
try:
    print(d["age"])
except KeyError:
    print("Key not found: age")

# LBYL Basics: Safe access with if key in dict
if "age" in d:
    print(d["age"])
else:
    print("Key not found: age")

# File Handling (EAFP): Try opening and catch FileNotFoundError
try:
    with open("important_notes.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")

# Attribute Access (EAFP): Use getattr() with fallback


class User:
    def __init__(self, name):
        self.name = name


u = User("Fiona")
print(getattr(u, "email", "No email provided"))

# LBYL Pitfall
filename = "data.txt"
if os.path.exists(filename):
    with open(filename) as f:
        data = f.read()

# Safe Type Conversion (EAFP style)
user_input = "abc"
try:
    num = int(user_input)
except ValueError:
    num = 0
print(num)  # 0
