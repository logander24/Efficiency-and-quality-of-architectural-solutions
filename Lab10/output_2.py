class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

class LibraryBookManager:
    def __init__(self, library_book):
        self.library_book = library_book

    def check_out(self):
        return self.library_book.check_out()

    def return_book(self):
        return self.library_book.return_book()

    def get_book_info(self):
        return {
            "title": self.library_book.title,
            "author": self.library_book.author,
            "publication_year": self.library_book.publication_year,
            "is_checked_out": self.library_book.is_checked_out
        }

    def check_condition(self):
        # Тут можна додати логіку для перевірки стану книги
        return "Стан книги: Добрий"

# Використання коду
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book_manager = LibraryBookManager(book)
print(book_manager.check_out())
print(book_manager.get_book_info())
print(book_manager.check_condition())
print(book_manager.return_book())
