from pathlib import Path
import os
import shutil
import tempfile
# 1. Read a File with pathlib

content = Path("myfile.txt").read_text()
print(content)

# 2. List All Python Files in the Current Directory
py_files = list(Path(".").glob("*.py"))
print(py_files)


# 3. Write "hello" to a File
("hello.txt").write_text("hello")
with open("hello.txt", "w") as f:
    f.write("hello")

# 4. Create & Delete Directory Safely (inside temp dir)
with tempfile.TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "new_folder")
    os.makedirs(path)
    print("Created:", path)
    shutil.rmtree(path)
    print("Deleted:", path)

# 5. Temporary File Usage
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
    temp_file.write("Testing...")
    temp_file.seek(0)
    print(temp_file.read())

# 6. Copy Files with shutil
shutil.copy("hello.txt", "hello_copy.txt")

# 7. Absolute vs Relative Path

path = Path("hello.txt")
print("Relative:", path)
print("Absolute:", path.resolve())

# 8. Check File Existence
path = Path("hello.txt")
print("Exists:", path.exists())
print("Is File:", path.is_file())
