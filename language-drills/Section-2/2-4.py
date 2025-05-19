import contextlib
import time
from contextlib import suppress
import tempfile
# Basic File Context
with open("example.txt", "r") as f:
    contents = f.read()
    print(contents)

# Multiple Contexts
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    print(f1.read())
    print(f2.read())

# Custom Context Manager (Class Version)


class Logger:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")


with Logger():
    print("Doing something inside")


# Custom Context Manager with @contextlib.contextmanager
@contextlib.contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Took {end - start:.4f} seconds")


with timer():
    sum(range(1000000))

# Suppressing Exceptions
with suppress(FileNotFoundError):
    with open("nonexistent.txt") as f:
        print(f.read())

# Temporary File
with tempfile.TemporaryFile() as tmp:
    tmp.write(b"Fi was here.")
    tmp.seek(0)
    print(tmp.read())


# Locking with Class
class DBConnection:
    def __enter__(self):
        print("Opening DB connection")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing DB connection")


with DBConnection():
    print("Running queries")


# Ensure Cleanup on Error
class Cleaner:
    def __enter__(self):
        print("Setup")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleanup always runs, even after error.")


with Cleaner():
    raise Exception("Something broke")
