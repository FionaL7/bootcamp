import time
# Basic Function Decorator


def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper


@simple_logger
def greet():
    print("Hello!")


greet()

# 2. Decorator with Arguments – prefix_printer


def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@prefix_printer("Calling")
def say_hi():
    print("Hi!")


say_hi()

# 3. Timing Decorator


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def wait():
    time.sleep(1)


wait()

# 4. Memoization Decorator


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


print(fib(30))

# 5. Debug Info Decorator


def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@debug_info
def add(a, b):
    return a + b


add(3, 5)

# 6. Access Control Decorator


def role_required(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                print("Access denied.")
                return
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


@role_required("admin")
def delete_post(user, post_id):
    print(f"Post {post_id} deleted.")


user = {"name": "Fiona", "role": "admin"}
delete_post(user, 42)

# 7. Retry Mechanism


def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
            print("All attempts failed.")
        return wrapper
    return decorator


@retry(3)
def flaky():
    import random
    if random.choice([True, False]):
        raise ValueError("Oops!")
    return "Success"


print(flaky())

# 8. Logging with Params


def custom_logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} - Starting {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{message} - Finished {func.__name__}")
            return result
        return wrapper
    return decorator


@custom_logger("LOG")
def greet_user(name):
    print(f"Hello, {name}")


greet_user("Fiona")

# 9. Class Method Decorator


def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if not args:
            raise ValueError("Arguments required")
        return func(self, *args, **kwargs)
    return wrapper


class Calculator:
    @validate_args
    def divide(self, x, y):
        return x / y


calc = Calculator()
print(calc.divide(10, 2))

# 10. Composition of Decorators


@simple_logger
@timer
@debug_info
def compute_sum(n):
    return sum(range(n))


compute_sum(100000)
