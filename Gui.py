import tkinter as tk
from tkinter import simpledialog, messagebox 
from Book import Book
from BookManager import BookManager
from DataPersistence import DataPersistence

class BookManagementGUI:
    def __init__(self, master, book_manager, data_persistence):
        self.master = master
        self.book_manager = book_manager
        self.data_persistence = data_persistence

        self.master.title("Book Management System")
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label = tk.Label(self.master, text="Book Management System")
        self.label.grid(row=0, column=1, pady=10)

        # Buttons
        self.add_button = tk.Button(self.master, text="Add Book", command=self.add_book)
        self.add_button.grid(row=1, column=0, pady=5, padx=5)

        self.search_button = tk.Button(self.master, text="Search Book", command=self.search_book)
        self.search_button.grid(row=1, column=1, pady=5, padx=5)

        self.update_button = tk.Button(self.master, text="Update Book", command=self.update_book)
        self.update_button.grid(row=1, column=2, pady=5, padx=5)

        self.delete_button = tk.Button(self.master, text="Delete Book", command=self.delete_book)
        self.delete_button.grid(row=1, column=3, pady=5, padx=5)

        self.display_button = tk.Button(self.master, text="Display All Books", command=self.display_all_books)
        self.display_button.grid(row=1, column=4, pady=5, padx=5)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_program)
        self.exit_button.grid(row=1, column=5, pady=5, padx=5)

    def add_book(self):
        isbn = simpledialog.askstring("Input", "Enter ISBN:")
        title = simpledialog.askstring("Input", "Enter Title:")
        author = simpledialog.askstring("Input", "Enter Author:")
        genre = simpledialog.askstring("Input", "Enter Genre:")

        new_book = Book(isbn, title, author, genre)
        self.book_manager.add_book(new_book)

        messagebox.showinfo("Success", "Book added successfully!")

    def search_book(self):
        key_attribute = simpledialog.askstring("Input", "Enter key attribute to search:")
        non_key_attribute = simpledialog.askstring("Input", f"Enter {key_attribute}:")
        found_book = self.book_manager.search_book(key_attribute, non_key_attribute)

        if found_book:
            messagebox.showinfo("Search Result", f"Book found: {found_book.title} by {found_book.author}")
        else:
            messagebox.showinfo("Search Result", "Book not found.")

    def update_book(self):
        isbn = simpledialog.askstring("Input", "Enter ISBN of the book to update:")
        attribute_to_update = simpledialog.askstring("Input", "Enter attribute to update:")
        new_value = simpledialog.askstring("Input", f"Enter new {attribute_to_update}:")

        success = self.book_manager.update_book(isbn, {attribute_to_update: new_value})
        if success:
            messagebox.showinfo("Success", "Book updated successfully!")
        else:
            messagebox.showinfo("Error", "Book not found.")

    def delete_book(self):
        isbn = simpledialog.askstring("Input", "Enter ISBN of the book to delete:")

        success = self.book_manager.delete_book(isbn)
        if success:
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            messagebox.showinfo("Error", "Book not found.")

    def display_all_books(self):
        books = "\n".join(self.book_manager.display_all_books())
        messagebox.showinfo("All Books", books)

    def exit_program(self):
        # Save data and exit
        self.data_persistence.save_data("books.json", [book.__dict__ for book in self.book_manager.books])
        self.master.destroy()

# main.py
if __name__ == "__main__":
    root = tk.Tk()
    book_manager = BookManager()
    data_persistence = DataPersistence()

    # Load existing data
    book_manager.books = data_persistence.load_data("books.json")

    gui = BookManagementGUI(root, book_manager, data_persistence)
    root.mainloop()