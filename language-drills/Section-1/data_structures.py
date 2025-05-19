# List Operations
a = [5, 3, 8]
a.append(2)       # [5, 3, 8, 2]
a.remove(3)       # [5, 8, 2]
a.sort()          # [2, 5, 8]
print(a)

# List Slicing
lst = [1, 2, 3, 4, 5, 6, 7]
middle_three = lst[2:5]   # [3, 4, 5]
print(middle_three)

# List Copying Pitfall
a = [1, 2, 3]
b = a          # both point to same list
b.append(4)
print("a after b.append:", a)  # a is changed too

a = [1, 2, 3]
b = a[:]       # this makes a copy
b.append(4)
print("a after b.append:", a)  # a remains unchanged

# Dictionary Access
user = {"name": "Alice"}

# Using .get()
age = user.get("age", "Not Found")  # returns "Not Found"
print("Age:", age)

# Using .setdefault()
user.setdefault("age", 25)  # adds "age" only if not present
print(user)

# Dictionary Iteration
person = {"name": "Bob", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# Set Operations
a = {1, 2, 3}
b = {3, 4}
print("Intersection:", a & b)   # {3}
print("Union:", a | b)          # {1, 2, 3, 4}
print("Difference:", a - b)     # {1, 2}

# Tuple Unpacking
t = (7, 8, 9)
x, y, z = t
print(x, y, z)  # 7 8 9

# Immutable Tuples
t = (1, 2, 3)
try:
    t[0] = 99  # TypeError expected
except TypeError as e:
    print("Error:", e)
