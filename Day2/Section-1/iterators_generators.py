# Manual Iterator
lst = [10, 20, 30]
it = iter(lst)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

# Custom Iterator Class: Counter(n)


class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration


for i in Counter(3):
    print(i)  # 1, 2, 3

# StopIteration Manually Raised and Caught
try:
    raise StopIteration("Done!")
except StopIteration as e:
    print("Caught StopIteration:", e)

# Simple Generator: countdown(n)


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for num in countdown(3):
    print(num)  # 3, 2, 1

# Generator with State: Running Totals


def running_total(nums):
    total = 0
    for n in nums:
        total += n
        yield total


for val in running_total([1, 2, 3]):
    print(val)  # 1, 3, 6

# Generator with .send()


def custom_accumulator():
    total = 0
    while True:
        num = yield total
        if num is not None:
            total += num


gen = custom_accumulator()
print(next(gen))      # Start the generator (prints 0)
print(gen.send(5))    # 5
print(gen.send(10))   # 15

# Generator Expression: Evens from range(10)
evens = (x for x in range(10) if x % 2 == 0)
for e in evens:
    print(e)  # 0, 2, 4, 6, 8

# Compare Generator vs List Comprehension
lst = [x for x in range(5) if x % 2 == 0]
gen = (x for x in range(5) if x % 2 == 0)
print("List:", lst)              # [0, 2, 4]
print("Generator:", list(gen))  # [0, 2, 4]
