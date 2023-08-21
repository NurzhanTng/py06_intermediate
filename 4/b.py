"""
Агрегация
"""

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: list[Book] = []
    
    def add_book(self, book):
        self.books.append(book)


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author


library = Library('Central Library')
b1 = Book("War and Mir", "Lev Tolstoi")
b2 = Book("War and Mir 2", "Lev Tolstoi")

library.add_book(b1)
library.add_book(b2)