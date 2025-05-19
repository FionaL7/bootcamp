# Pass Function as Argument
def apply(func, value):
    return func(value)


print(apply(abs, -5))  # 5
print(apply(str.upper, "hello"))  # HELLO

# Return Function from Function


def make_doubler():
    return lambda x: x * 2


doubler = make_doubler()
print(doubler(5))  # 10

# Store Functions in a List
funcs = [abs, str, hex]
results = [f(-42) for f in funcs]
print(results)  # [42, '-42', '-0x2a']

# Use map with Lambda (Squaring)
squared = list(map(lambda x: x ** 2, [1, 2, 3]))
print(squared)  # [1, 4, 9]

# Use filter with Lambda (Even Numbers)
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)  # [0, 2, 4, 6, 8]

# Sort with Lambda Key
pairs = [(1, "b"), (2, "a")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(2, 'a'), (1, 'b')]

# Inline Function Composition


def compose(f, g):
    return lambda x: f(g(x))


def double(x): return x * 2
def increment(x): return x + 1


composed = compose(double, increment)  # (x+1)*2
print(composed(3))  # 8

# Closure with Lambda


def make_multiplier(factor):
    return lambda x: x * factor


triple = make_multiplier(3)
print(triple(4))  # 12
