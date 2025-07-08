class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []
        pass

    def add_book(self, book):
        self._books.append(book)
        pass

    def check_out_book(self, title):
        pass

    def return_book(self, title):
        pass

    def list_available_books(self):
        pass


