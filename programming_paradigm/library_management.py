class Book:
    def __init__(self, title=None, author=None):
        self.title = title
        self.author = author
        self. __is_checked_out = False

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def available(self):
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        # book = Book(title=title)
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.check_out()
                break

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.return_book()
                break

    def list_available_books(self):
        for book in self.__books:
            if book.available():
                print(f"{book.title} by {book.author}")
