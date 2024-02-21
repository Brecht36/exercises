class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for item in self.books:
            if (item.title == book.title and item.author == book.author):
                self.books.remove(item)

    def search_books(self, search_string):
        new_list = []
        for item in self.books:
            if search_string.lower() in item.title.lower() or search_string.lower() in item.author.lower():
                new_list.append(item)
        return new_list
