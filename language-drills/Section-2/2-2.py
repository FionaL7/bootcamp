# Enumerate
items = ['apple', 'banana', 'cherry']
for index, value in enumerate(items):
    print(index, value)

# Zip
nums = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = list(zip(nums, letters))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# any / all
numbers = [1, 2, -3, 4]
print(any(n < 0 for n in numbers))
print(all(n > 0 for n in numbers))

# sorted with key
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(4, 1), (2, 2), (1, 3)]

# map and filter
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]
filtered = list(filter(lambda x: x % 2 != 0, nums))
print(filtered)  # [1, 3]

# Chained Comparison
x = 5
if 0 < x < 10:
    print("x is between 0 and 10")
a = 10
b = 20
a, b = b, a
print(a, b)  # 20, 10

# Unpacking in Loops
pairs = [(1, 2), (3, 4)]
for x, y in pairs:
    print(f"x: {x}, y: {y}")
