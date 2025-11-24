# FILE: database.py
# PURPOSE: Manages all interactions with the SQLite database (library.db).

import sqlite3
from datetime import date

# Sets up the database and creates tables if they don't exist
def create_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    # The 'books' table stores the main information for each book
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            isbn TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            status TEXT,
            cover_url TEXT
        )
    ''')
    # The 'issued_books' table tracks which book is loaned to whom
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS issued_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT,
            student_name TEXT,
            issue_date DATE
        )
    ''')
    conn.commit()
    conn.close()

# Adds a new book record to the database
def add_new_book(isbn, title, author, cover_url):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO books (isbn, title, author, status, cover_url) VALUES (?, ?, ?, ?, ?)",
                       (isbn, title, author, 'Available', cover_url))
        conn.commit()
        conn.close()
        return f"Success! Added '{title}'."
    except sqlite3.IntegrityError:
        conn.close()
        return f"Error! Book with ISBN {isbn} already exists."

# Issues a book 
def issue_a_book(isbn, student_name):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM books WHERE isbn = ?", (isbn,))
    result = cursor.fetchone()
    if result and result[0] == 'Available':
        cursor.execute("UPDATE books SET status = 'Issued' WHERE isbn = ?", (isbn,))
        today = date.today()
        cursor.execute("INSERT INTO issued_books (isbn, student_name, issue_date) VALUES (?, ?, ?)", (isbn, student_name, today))
        conn.commit()
        conn.close()
        return f"Success! Book issued to {student_name}."
    else:
        conn.close()
        return "Error! Book is unavailable or doesn't exist."

# Returns a book to the library 
def return_a_book(isbn):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM books WHERE isbn = ?", (isbn,))
    result = cursor.fetchone()
    if result and result[0] == 'Issued':
        cursor.execute("UPDATE books SET status = 'Available' WHERE isbn = ?", (isbn,))
        cursor.execute("DELETE FROM issued_books WHERE isbn = ?", (isbn,))
        conn.commit()
        conn.close()
        return "Success! Book returned to the library."
    else:
        conn.close()
        return "Error! This book was not issued."

# Retrieves all books from the database
def view_all_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT isbn, title, author, status FROM books ORDER BY title")
    books = cursor.fetchall()
    conn.close()
    return books

# Retrieves all currently issued books
def view_issued_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT b.title, i.student_name, i.issue_date, b.isbn
        FROM issued_books i JOIN books b ON i.isbn = b.isbn
        ORDER BY i.issue_date
    ''')
    issued = cursor.fetchall()
    conn.close()
    return issued