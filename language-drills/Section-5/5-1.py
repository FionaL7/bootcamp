from collections import defaultdict, Counter, deque, OrderedDict

# 1. defaultdict for Grouping by First Letter
words = ["apple", "ant", "banana", "bear", "carrot"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
# {'a': ['apple', 'ant'], 'b': ['banana', 'bear'], 'c': ['carrot']}

# 2. Counter Basics
freq = Counter("hello world")
print(freq)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 3. Most Common Elements
numbers = [1, 2, 2, 3, 3, 3, 4]
common = Counter(numbers).most_common(2)
print(common)
# [(3, 3), (2, 2)]

# 4. deque for Stack & Queue
d = deque()
# Simulate Queue (FIFO)
d.append("first")
d.append("second")
print(d.popleft())  # 'first'

# Simulate Stack (LIFO)
d.append("third")
print(d.pop())      # 'third'

# 5. Rotate a deque
d = deque([1, 2, 3, 4, 5])
d.rotate(2)
print(d)  # deque([4, 5, 1, 2, 3])

# 6. OrderedDict Iteration
ordered = OrderedDict()
ordered["one"] = 1
ordered["two"] = 2
ordered["three"] = 3

for key, val in ordered.items():
    print(key, val)
# one 1
# two 2
# three 3

# 7. Defaultdict with Lambda
d = defaultdict(lambda: "N/A")
d["name"] = "Fipna"
print(d["name"])
print(d["missing"])  # N/A

# 8. Nested defaultdict
# defaultdict(dict)
nested = defaultdict(dict)
nested["user1"]["score"] = 90
print(nested)

# defaultdict of defaultdict(int)
nested_int = defaultdict(lambda: defaultdict(int))
nested_int["user2"]["likes"] += 1
print(nested_int)
