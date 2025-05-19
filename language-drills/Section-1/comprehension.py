import sys
# List Comprehension with Condition
nums = [1, 2, 3, 4]
squares_of_evens = [x**2 for x in nums if x % 2 == 0]  # [4, 16]
print(squares_of_evens)

# Nested List Comprehension (Flatten)
nested = [[1, 2], [3, 4]]
flattened = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4]
print(flattened)

# Dictionary Comprehension
chars = ["a", "b"]
char_dict = {char: 1 for char in chars}  # {'a': 1, 'b': 1}
print(char_dict)

# Set Comprehension
text = "hello world"
vowels = {ch for ch in text if ch in "aeiou"}  # {'e', 'o'}
print(vowels)

# Generator Expression
gen = (n * n for n in range(5))
for val in gen:
    print(val)  # 0, 1, 4, 9, 16

# List vs Generator
list_obj = [x for x in range(1000000)]
gen_obj = (x for x in range(1000000))
print("List size:", sys.getsizeof(list_obj))  # Big
print("Generator size:", sys.getsizeof(gen_obj))  # Tiny


#  Filter with Comprehension
words = ["hi", "hello", "bye"]
even_length = [word for word in words if len(word) % 2 == 0]  # ['hi', 'bye']
print(even_length)

# Conditional Assignment in List Comprehension
nums = [4, -1, 7, -3, 0]
cleaned = [x if x >= 0 else 0 for x in nums]  # [4, 0, 7, 0, 0]
print(cleaned)
