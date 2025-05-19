from contextlib import suppress
# try/except: Basic Division By Zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")
# try/except/else:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Success")

# finally Block: Always Runs
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Cleanup done")  # Always runs, even if error

# Multiple Exceptions
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Zero division error")

# Custom Exception


class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")


try:
    check_age(-5)
except InvalidAgeError as e:
    print("Custom Error:", e)

# Reraise Exception (After Logging or Cleanup)
try:
    1 / 0
except ZeroDivisionError as e:
    print("Logging error:", e)
    raise  # Re-raises the exception again

# Suppressing Exceptions (contextlib.suppress)
d = {"a": 1}
with suppress(KeyError):
    print(d["b"])  # Silently ignored

# Nested try Blocks
try:
    try:
        x = int("oops")
    except ValueError:
        print("Inner: ValueError caught")
        raise
except Exception as e:
    print("Outer caught:", e)
