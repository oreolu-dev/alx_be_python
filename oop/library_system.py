class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    # creating books (a list to store instances of Book, EBook, and PrintBook).
    def __init__(self,):
        self.books = []

    #  based on the Library class (self.books); add_book(self, book) adds a Book, EBook, or PrintBook instance to the library.
    def add_book(self, book):
        self.books.append(book)

    # Prints details of each book in the library
    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Pages: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")