# Define a Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Create an Object
book1 = Book("1984", "Orwell")
print(book1.title)
print(book1.author)


# Add a Method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"


print(book1.describe())

# Class vs Instance Variable


class Book:
    category = "Fiction"

    def __init__(self, title, author):
        self.title = title
        self.author = author


book2 = Book("Brave New World", "Huxley")
print(book2.category)

# Update Object State


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def update_title(self, new_title):
        self.title = new_title


book2.update_title("New Brave World")
print(book2.title)

# init Logic with Defaults


class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author


book3 = Book()
print(book3.describe())


# Dynamic Attribute
book3.publisher = "Penguin"
print(book3.publisher)

# Check Type
print(isinstance(book1, Book))
print(isinstance(book3, Book))
