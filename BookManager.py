class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, key_attribute, non_key_attribute):
        for book in self.books:
            if getattr(book, key_attribute) == non_key_attribute:
                return book
        return None

    def update_book(self, isbn, new_attributes):
        for book in self.books:
            if book.isbn == isbn:
                for key, value in new_attributes.items():
                    setattr(book, key, value)
                return True
        return False

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def display_all_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
