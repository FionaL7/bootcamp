from functools import partial, lru_cache,  wraps, reduce
import time
from collections import defaultdict

# 1. partial()
binary_to_int = partial(int, base=2)
print(binary_to_int("1010"))  # 10


# 2. @lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print(fib(30))  # Fast af

# 3. Preserve Function Metadata with @wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@decorator
def greet():
    """This says hello."""
    print("Hello Aaron!")


print(greet.__name__)     # greet
print(greet.__doc__)      # This says hello.

# 4. Chained Partials – Build a Custom Print
print_newline = partial(print, end="\n\n")
print_upper = partial(print_newline, sep=" | ")
print_final = partial(print_upper, "🔊")

print_final("Aaron", "is", "awesome")

# 5. Compare Recursive Fib: Cached vs Uncached


def fib_uncached(n):
    if n < 2:
        return n
    return fib_uncached(n-1) + fib_uncached(n-2)


start = time.time()
fib_uncached(30)
print("Uncached:", time.time() - start)


@lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n-1) + fib_cached(n-2)


start = time.time()
fib_cached(30)
print("Cached:", time.time() - start)

# 6. reduce() with Lambda


def factorial(n): return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(5))  # 120

# 7. Default Dict Generator


def nested_dict(): return defaultdict(partial(defaultdict, dict))


data = nested_dict()
data['fi']['space'] = {'stars': 100}
print(data['fi']['space'])  # {'stars': 100}

# 8. Logging Decorator with wraps


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Start: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] End: {func.__name__}")
        return result
    return wrapper


@log_decorator
def multiply(a, b):
    return a * b


print(multiply(2, 5))
