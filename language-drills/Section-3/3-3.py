# __str__ vs __repr__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}' (pretty)"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


book = Book("1984", "Orwell")
print(book)     # Calls __str__ (friendly)
book            # Calls __repr__ (official)

# Equality Check: __eq__


def __eq__(self, other):
    if isinstance(other, Book):
        return self.title == other.title and self.author == other.author
    return False


b1 = Book("1984", "Orwell")
b2 = Book("1984", "Orwell")
print(b1 == b2)  # True

# Hashing Support: __hash__


def __hash__(self):
    return hash((self.title, self.author))


book_set = {b1, b2}
print(len(book_set))

# Ordering Support: __lt__


def __lt__(self, other):
    return self.title < other.title


books = [Book("Zebra", "X"), Book("Animal Farm", "Orwell")]
sorted_books = sorted(books)
for b in sorted_books:
    print(b)


# Custom Container: __len__ in Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)


lib = Library()
lib.add_book(Book("1984", "Orwell"))
print(len(lib))  # 1

# Indexing Support: __getitem__


def __getitem__(self, index):
    return self.books[index]


print(lib[0])
