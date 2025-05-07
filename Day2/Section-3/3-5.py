import json
# Base Setup


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Static Method: Validate ISBN
    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and len(isbn.replace('-', '')) == 13


# Class Method: Parse "Title|Author"


    @classmethod
    def from_string(cls, s):
        title, author = s.split('|')
        return cls(title.strip(), author.strip())


b = Book.from_string("1984 | Orwell")
print(Book.is_valid_isbn("978-3-16-148410-0"))  # True
print(Book().is_valid_isbn("978-3"))
print(b.title, b.author)  # 1984 Orwell

# Use cls in Subclass Too


class Novel(Book):
    def __init__(self, title, author, genre="Unknown"):
        super().__init__(title, author)
        self.genre = genre


n = Novel.from_string("Dune | Frank Herbert")
print(isinstance(n, Novel))  # True


# Difference in Behavior: Static vs Class
class Test:
    @staticmethod
    def static_method():
        print("No self or cls here")

    @classmethod
    def class_method(cls):
        print(f"Hello from {cls.__name__}")


Test.class_method()

# Alternative Constructors


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['author'])

    @classmethod
    def from_json(cls, json_str):
        return cls.from_dict(json.loads(json_str))


book1 = Book.from_dict({'title': 'The Hobbit', 'author': 'Tolkien'})
book2 = Book.from_json('{"title": "Dracula", "author": "Stoker"}')

# Static Method Call: Class vs Instance
print(Book.is_valid_isbn("1234567890123"))
print(book1.is_valid_isbn("1234567890123"))

# Method Resolution: Override Class Method


class Base:
    @classmethod
    def who(cls):
        return f"Base class: {cls.__name__}"


class Sub(Base):
    @classmethod
    def who(cls):
        return f"Sub class: {cls.__name__}"


print(Base.who())  # Base class: Base
print(Sub.who())   # Sub class: Sub


# Hybrid Method Example
class LibraryBook:
    total_books = 0

    def __init__(self, title):
        self.title = title
        LibraryBook.total_books += 1

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title) > 0

    @classmethod
    def report(cls):
        return f"{cls.total_books} books total"

    def describe(self):
        return f"Book: {self.title}"


lb = LibraryBook("Matilda")
print(LibraryBook.report())             # class method
print(lb.describe())                    # instance method
print(LibraryBook.is_valid_title(""))   # static method
