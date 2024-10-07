import cx_Oracle
import tkinter as tk
from tkinter import messagebox

# Connect to the Oracle XE database
connection = cx_Oracle.connect("SYSTEM/tista@localhost:1521/xe")
cursor = connection.cursor()

# Function to add a book
def add_book():
    def submit():
        book_id = int(entry_book_id.get())
        title = entry_title.get()
        author_name = entry_author_name.get()
        published_date = entry_published_date.get()
        available_copies = int(entry_available_copies.get())

        cursor.execute("INSERT INTO books (book_id, title, author_name, published_date, available_copies) VALUES (:book_id, :title, :author_name, TO_DATE(:published_date, 'YYYY-MM-DD'), :available_copies)",
                       {"book_id": book_id, "title": title, "author_name": author_name, "published_date": published_date, "available_copies": available_copies})
        connection.commit()
        messagebox.showinfo("Success", "Book added successfully")
        add_book_window.destroy()

    add_book_window = tk.Toplevel(root)
    add_book_window.title("Add Book")

    tk.Label(add_book_window, text="Book ID:").grid(row=0, column=0)
    tk.Label(add_book_window, text="Title:").grid(row=1, column=0)
    tk.Label(add_book_window, text="Author Name:").grid(row=2, column=0)
    tk.Label(add_book_window, text="Published Date (YYYY-MM-DD):").grid(row=3, column=0)
    tk.Label(add_book_window, text="Available Copies:").grid(row=4, column=0)

    entry_book_id = tk.Entry(add_book_window)
    entry_title = tk.Entry(add_book_window)
    entry_author_name = tk.Entry(add_book_window)
    entry_published_date = tk.Entry(add_book_window)
    entry_available_copies = tk.Entry(add_book_window)

    entry_book_id.grid(row=0, column=1)
    entry_title.grid(row=1, column=1)
    entry_author_name.grid(row=2, column=1)
    entry_published_date.grid(row=3, column=1)
    entry_available_copies.grid(row=4, column=1)

    tk.Button(add_book_window, text="Submit", command=submit).grid(row=5, column=1)

# Function to update a book
def update_book():
    def submit():
        book_id = int(entry_book_id.get())
        title = entry_title.get()
        author_name = entry_author_name.get()
        published_date = entry_published_date.get()
        available_copies = int(entry_available_copies.get())

        cursor.execute("UPDATE books SET title=:title, author_name=:author_name, published_date=TO_DATE(:published_date, 'YYYY-MM-DD'), available_copies=:available_copies WHERE book_id=:book_id",
                       {"book_id": book_id, "title": title, "author_name": author_name, "published_date": published_date, "available_copies": available_copies})
        connection.commit()
        messagebox.showinfo("Success", "Book updated successfully")
        update_book_window.destroy()

    update_book_window = tk.Toplevel(root)
    update_book_window.title("Update Book")

    tk.Label(update_book_window, text="Book ID:").grid(row=0, column=0)
    tk.Label(update_book_window, text="Title:").grid(row=1, column=0)
    tk.Label(update_book_window, text="Author Name:").grid(row=2, column=0)
    tk.Label(update_book_window, text="Published Date (YYYY-MM-DD):").grid(row=3, column=0)
    tk.Label(update_book_window, text="Available Copies:").grid(row=4, column=0)

    entry_book_id = tk.Entry(update_book_window)
    entry_title = tk.Entry(update_book_window)
    entry_author_name = tk.Entry(update_book_window)
    entry_published_date = tk.Entry(update_book_window)
    entry_available_copies = tk.Entry(update_book_window)

    entry_book_id.grid(row=0, column=1)
    entry_title.grid(row=1, column=1)
    entry_author_name.grid(row=2, column=1)
    entry_published_date.grid(row=3, column=1)
    entry_available_copies.grid(row=4, column=1)

    tk.Button(update_book_window, text="Submit", command=submit).grid(row=5, column=1)

# Function to delete a book
def delete_book():
    def submit():
        book_id = int(entry_book_id.get())

        cursor.execute("DELETE FROM books WHERE book_id=:book_id", {"book_id": book_id})
        connection.commit()
        messagebox.showinfo("Success", "Book deleted successfully")
        delete_book_window.destroy()

    delete_book_window = tk.Toplevel(root)
    delete_book_window.title("Delete Book")

    tk.Label(delete_book_window, text="Book ID:").grid(row=0, column=0)

    entry_book_id = tk.Entry(delete_book_window)
    entry_book_id.grid(row=0, column=1)

    tk.Button(delete_book_window, text="Submit", command=submit).grid(row=1, column=1)

# Function to add a borrower
def add_borrower():
    def submit():
        borrower_id = int(entry_borrower_id.get())
        name = entry_name.get()
        contact = entry_contact.get()

        cursor.execute("INSERT INTO borrowers (borrower_id, name, contact) VALUES (:borrower_id, :name, :contact)",
                       {"borrower_id": borrower_id, "name": name, "contact": contact})
        connection.commit()
        messagebox.showinfo("Success", "Borrower added successfully")
        add_borrower_window.destroy()

    add_borrower_window = tk.Toplevel(root)
    add_borrower_window.title("Add Borrower")

    tk.Label(add_borrower_window, text="Borrower ID:").grid(row=0, column=0)
    tk.Label(add_borrower_window, text="Name:").grid(row=1, column=0)
    tk.Label(add_borrower_window, text="Contact:").grid(row=2, column=0)

    entry_borrower_id = tk.Entry(add_borrower_window)
    entry_name = tk.Entry(add_borrower_window)
    entry_contact = tk.Entry(add_borrower_window)

    entry_borrower_id.grid(row=0, column=1)
    entry_name.grid(row=1, column=1)
    entry_contact.grid(row=2, column=1)

    tk.Button(add_borrower_window, text="Submit", command=submit).grid(row=3, column=1)

# Function to borrow a book
def borrow_book():
    def submit():
        record_id = int(entry_record_id.get())
        book_id = int(entry_book_id.get())
        borrower_id = int(entry_borrower_id.get())
        borrow_date = entry_borrow_date.get()

        cursor.execute("INSERT INTO borrow_records (record_id, book_id, borrower_id, borrow_date, return_date) VALUES (:record_id, :book_id, :borrower_id, TO_DATE(:borrow_date, 'YYYY-MM-DD'), NULL)",
                       {"record_id": record_id, "book_id": book_id, "borrower_id": borrower_id, "borrow_date": borrow_date})
        cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE book_id = :book_id", {"book_id": book_id})
        connection.commit()
        messagebox.showinfo("Success", "Book borrowed successfully")
        borrow_book_window.destroy()

    borrow_book_window = tk.Toplevel(root)
    borrow_book_window.title("Borrow Book")

    tk.Label(borrow_book_window, text="Record ID:").grid(row=0, column=0)
    tk.Label(borrow_book_window, text="Book ID:").grid(row=1, column=0)
    tk.Label(borrow_book_window, text="Borrower ID:").grid(row=2, column=0)
    tk.Label(borrow_book_window, text="Borrow Date (YYYY-MM-DD):").grid(row=3, column=0)

    entry_record_id = tk.Entry(borrow_book_window)
    entry_book_id = tk.Entry(borrow_book_window)
    entry_borrower_id = tk.Entry(borrow_book_window)
    entry_borrow_date = tk.Entry(borrow_book_window)

    entry_record_id.grid(row=0, column=1)
    entry_book_id.grid(row=1, column=1)
    entry_borrower_id.grid(row=2, column=1)
    entry_borrow_date.grid(row=3, column=1)

    tk.Button(borrow_book_window, text="Submit", command=submit).grid(row=4, column=1)

# Function to return a book
def return_book():
    def submit():
        record_id = int(entry_record_id.get())
        return_date = entry_return_date.get()

        cursor.execute("UPDATE borrow_records SET return_date = TO_DATE(:return_date, 'YYYY-MM-DD') WHERE record_id = :record_id",
                       {"record_id": record_id, "return_date": return_date})
        cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id = (SELECT book_id FROM borrow_records WHERE record_id = :record_id)", {"record_id": record_id})
        connection.commit()
        messagebox.showinfo("Success", "Book returned successfully")
        return_book_window.destroy()

    return_book_window = tk.Toplevel(root)
    return_book_window.title("Return Book")

    tk.Label(return_book_window, text="Record ID:").grid(row=0, column=0)
    tk.Label(return_book_window, text="Return Date (YYYY-MM-DD):").grid(row=1, column=0)

    entry_record_id = tk.Entry(return_book_window)
    entry_return_date = tk.Entry(return_book_window)

    entry_record_id.grid(row=0, column=1)
    entry_return_date.grid(row=1, column=1)

    tk.Button(return_book_window, text="Submit", command=submit).grid(row=2, column=1)

# Main application window
root = tk.Tk()
root.title("Library Management System")

tk.Button(root, text="Add Book", command=add_book).grid(row=0, column=0)
tk.Button(root, text="Update Book", command=update_book).grid(row=1, column=0)
tk.Button(root, text="Delete Book", command=delete_book).grid(row=2, column=0)
tk.Button(root, text="Add Borrower", command=add_borrower).grid(row=3, column=0)
tk.Button(root, text="Borrow Book", command=borrow_book).grid(row=4, column=0)
tk.Button(root, text="Return Book", command=return_book).grid(row=5, column=0)
tk.Button(root, text="Exit", command=root.quit).grid(row=6, column=0)

root.mainloop()

# Close the connection
connection.close()
