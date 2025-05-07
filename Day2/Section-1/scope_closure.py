# LEGB Rule (Local, Enclosing, Global, Built-in)
x = 10  # Global


def demo():
    x = 20  # Local
    print("Inside function:", x)


demo()              # Inside function: 20
print("Global x:", x)

# Nested Function Access (Enclosing Scope)


def outer():
    msg = "Hello from outer"

    def inner():
        print(msg)  # Accessing enclosing variable
    inner()


outer()

# nonlocal Keyword (Modifying Enclosing Variable)


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Count inside:", count)
    inner()
    inner()


outer()

# global Keyword (Modifying Global Variable)
counter = 0


def increase():
    global counter
    counter += 1


increase()
print("Global counter:", counter)  # Global counter: 1

# Closure Function (make_multiplier)


def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier


# Closure created here
triple = make_multiplier(3)
print(triple(10))  # 30

# Closure Memory
double = make_multiplier(2)
print(double(5))   # 10

# Name Shadowing
len = 5
try:
    print(len("hello"))  # ❌ TypeError
except TypeError as e:
    print("Oops:", e)

del len
print(len("hello"))  # ✅ Back to normal: 5

# Scope Error (Access Before Assignment)


def broken():
    try:
        print(x)  # UnboundLocalError!
        x = 5
    except UnboundLocalError as e:
        print("Caught Error:", e)


broken()
