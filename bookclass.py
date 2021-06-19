
class Book:
    def __init__(self, isbn, title, author, publisher):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f"{self.title}, {self.author}, {self.publisher}"