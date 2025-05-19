# Subclassing
class Novel(Book):
    pass

# Override Method


class Novel(Book):
    def describe(self):
        return f"Novel: '{self.title}' by {self.author}"


# Use super()
class Novel(Book):
    def describe(self):
        return "Novel: " + super().describe()

# Add New Attribute


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre


novel1 = Novel("Pride and Prejudice", "Austen", "Romance")
print(novel1.genre)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


print(Book("1984", "Orwell"))


# Multiple Inheritance
class AudioMixin:
    def play_audio(self):
        print(f"Playing audiobook: '{self.title}'")


class AudioBook(Book, AudioMixin):
    pass


audio_book = AudioBook("Becoming", "Michelle Obama")
audio_book.play_audio()


# isinstance with Inheritance
print(isinstance(novel1, Novel))  # True
print(isinstance(novel1, Book))   # Also True


# Polymorphism
books = [Book("1984", "Orwell"), Novel(
    "Pride and Prejudice", "Austen", "Romance")]

for b in books:
    print(b.describe())
