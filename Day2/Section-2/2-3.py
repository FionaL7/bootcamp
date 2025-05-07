
# Inline Conditional
x = 10
result = "High" if x > 5 else "Low"
print(result)  # High

# Chained Assignment
x = y = z = 0
print(x, y, z)  # 0 0 0

# Walrus Operator (:=)
while (line := input("Say something (type 'exit' to quit): ")) != "exit":
    print("You said:", line)

# Ternary in Function Call
flag = True
print("Yes" if flag else "No")  # Yes

# Multiple Unpack
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)  # 1 2 [3, 4, 5]

# Use or as Fallback
name = input("Enter your name: ") or "Anonymous"
print(name)

# Use and for Guarded Execution
is_admin = True
def delete_user(user_id): print(f"User {user_id} deleted.")


is_admin and delete_user(42)

# Conditional in Comprehensions
print(['even' if x % 2 == 0 else 'odd' for x in range(5)])
