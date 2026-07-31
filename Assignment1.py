class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully.")

    def borrow_book(self, patron_id, book_id):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if patron is None:
            print("Patron not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(patron.name, "borrowed", book.title)
        else:
            print("Book is already borrowed.")

    def return_book(self, patron_id, book_id):
        for p in self.patrons:
            if p.patron_id == patron_id:
                for b in p.borrowed_books:
                    if b.book_id == book_id:
                        b.available = True
                        p.borrowed_books.remove(b)
                        print(p.name, "returned", b.title)
                        return
                print("This book was not borrowed by the patron.")
                return

        print("Patron not found.")

    def show_books(self):
        print("\nLibrary Books")
        for b in self.books:
            if b.available:
                status = "Available"
            else:
                status = "Borrowed"

            print(b.book_id, "-", b.title, "-", b.author, "-", status)


# Main Program

library = Library()

library.add_book(Book(101, "Python Basics", "John"))
library.add_book(Book(102, "Data Structures", "David"))
library.add_book(Book(103, "Machine Learning", "Andrew"))

library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Priya"))

library.show_books()

print("\nBorrowing Book")
library.borrow_book(1, 101)

library.show_books()

print("\nReturning Book")
library.return_book(1, 101)

library.show_books()


comment(output)

Book added successfully.
Book added successfully.
Book added successfully.
Patron registered successfully.
Patron registered successfully.

Library Books
101 - Python Basics - John - Available
102 - Data Structures - David - Available
103 - Machine Learning - Andrew - Available

Borrowing Book
Rahul borrowed Python Basics

Library Books
101 - Python Basics - John - Borrowed
102 - Data Structures - David - Available
103 - Machine Learning - Andrew - Available

Returning Book
Rahul returned Python Basics

Library Books
101 - Python Basics - John - Available
102 - Data Structures - David - Available
103 - Machine Learning - Andrew - Available
