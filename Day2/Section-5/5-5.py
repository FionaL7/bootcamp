import subprocess
import time
import threading
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
# Run a Command (Platform Dependent)
# Linux/macOS:
subprocess.run(["ls", "-l"])
# Windows:
subprocess.run(["cmd", "/c", "dir"])

# Capture Output
result = subprocess.run(["echo", "hello Fi"], capture_output=True, text=True)
print("Captured:", result.stdout.strip())

# Check Exit Code
bad = subprocess.run(["ls", "nonexistent_file"], capture_output=True)
if bad.returncode != 0:
    print("Failed with code:", bad.returncode)
    print("Error:", bad.stderr.decode())

# Start a Thread


def greet():
    print("Hey from thread!")


t = threading.Thread(target=greet)
t.start()
t.join()

# Start a Process (Multiprocessing)


def say_hello():
    print("Hello from another process!")


p = Process(target=say_hello)
p.start()
p.join()

# Thread Locking
counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
print("Final counter:", counter)

# Use concurrent.futures ThreadPoolExecutor


def square(n):
    return n * n


with ThreadPoolExecutor() as executor:
    results = executor.map(square, [1, 2, 3, 4])
    print(list(results))

# Kill a Subprocess After Delay
proc = subprocess.Popen(["python", "-c", "import time; time.sleep(10)"])
time.sleep(2)
print("Terminating subprocess...")
proc.terminate()
proc.wait()
print("Done.")
