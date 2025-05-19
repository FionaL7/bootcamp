# Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")


greet("Fiona")     # Hello, Fi!
greet()

# Keyword Arguments (Flexible Ordering)


def info(name, age=0):
    print(f"{name} is {age} years old.")


info(age=25, name="Luna")  # Luna is 25 years old.
info(name="Nova")

# Variable Keyword Args (**kwargs)


def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_settings(theme="dark", font="Arial", size=12)
# theme: dark
# font: Arial
# size: 12

# Mixed Args (*args + **kwargs)


def magic_box(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


magic_box(1, 2, 3, mode="auto", debug=True)
# Positional: (1, 2, 3)


# Positional-Only Args (Python 3.8+)
def power(base, exponent, /):
    return base ** exponent


print(power(2, 3))  # 8

# Keyword-Only Args


def print_report(*, title, author):
    print(f"{title} by {author}")


print_report(title="The Void", author="Fiona")  # ✅

# Function Annotations (Type Hints)


def add(a: int, b: int) -> int:
    return a + b


print(add(3, 4))
