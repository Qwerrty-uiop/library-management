# FILE: app.py
# PURPOSE: This is the main application file. It creates the GUI and handles user interactions.

import customtkinter as ctk
import database
import google_books
from PIL import Image
import urllib.request
import io

# Main Application Class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cute Library Management System ")
        self.geometry("800x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.fetched_book_data = None
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.nav_frame = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.nav_frame.grid(row=0, column=0, sticky="nswe")
        self.nav_frame.grid_rowconfigure(5, weight=1)
        self.add_book_button = ctk.CTkButton(self.nav_frame, text="Add Book", command=self.show_add_book_frame)
        self.add_book_button.grid(row=0, column=0, padx=20, pady=20)
        self.issue_book_button = ctk.CTkButton(self.nav_frame, text="Issue/Return", command=self.show_issue_return_frame)
        self.issue_book_button.grid(row=1, column=0, padx=20, pady=20)
        self.view_all_button = ctk.CTkButton(self.nav_frame, text="View All Books", command=self.show_view_all_frame)
        self.view_all_button.grid(row=2, column=0, padx=20, pady=20)
        self.view_issued_button = ctk.CTkButton(self.nav_frame, text="View Issued", command=self.show_view_issued_frame)
        self.view_issued_button.grid(row=3, column=0, padx=20, pady=20)
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.show_add_book_frame()

    def clear_content_frame(self):
        self.fetched_book_data = None
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_add_book_frame(self):
        self.clear_content_frame()
        ctk.CTkLabel(self.content_frame, text="Add a New Book", font=("Arial", 20)).pack(pady=10)
        self.isbn_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Enter 13-Digit ISBN")
        self.isbn_entry.pack(pady=10, padx=20, fill="x")
        self.fetch_button = ctk.CTkButton(self.content_frame, text="Fetch Book Info", command=self.fetch_book_details)
        self.fetch_button.pack(pady=10)
        self.status_label = ctk.CTkLabel(self.content_frame, text="")
        self.status_label.pack(pady=10)
        self.book_info_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.book_info_frame.pack(pady=20, padx=20, fill="both", expand=True)

    def show_issue_return_frame(self):
        self.clear_content_frame()
        ctk.CTkLabel(self.content_frame, text="Issue or Return a Book", font=("Arial", 20)).pack(pady=10)
        self.issue_isbn_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Enter Book ISBN")
        self.issue_isbn_entry.pack(pady=10, padx=20, fill="x")
        self.student_name_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Enter Student Name (for issuing)")
        self.student_name_entry.pack(pady=10, padx=20, fill="x")
        button_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text="Issue Book", command=self.issue_book).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Return Book", command=self.return_book, fg_color="#C04040").pack(side="left", padx=10)
        self.issue_status_label = ctk.CTkLabel(self.content_frame, text="")
        self.issue_status_label.pack(pady=10)

    def show_view_all_frame(self):
        self.clear_content_frame()
        ctk.CTkLabel(self.content_frame, text="All Books in the Library", font=("Arial", 20)).pack(pady=10)
        books = database.view_all_books()
        if not books:
            ctk.CTkLabel(self.content_frame, text="The library is empty!").pack(pady=10)
            return
        for book in books:
            book_text = f"'{book[1]}' by {book[2]} (ISBN: {book[0]}) - Status: {book[3]}"
            ctk.CTkLabel(self.content_frame, text=book_text, wraplength=500).pack(anchor="w", padx=10)

    def show_view_issued_frame(self):
        self.clear_content_frame()
        ctk.CTkLabel(self.content_frame, text="Currently Issued Books", font=("Arial", 20)).pack(pady=10)
        issued_books = database.view_issued_books()
        if not issued_books:
            ctk.CTkLabel(self.content_frame, text="No books are currently issued.").pack(pady=10)
            return
        for book in issued_books:
            book_text = f"'{book[0]}' issued to {book[1]} on {book[2]} (ISBN: {book[3]})"
            ctk.CTkLabel(self.content_frame, text=book_text, wraplength=500).pack(anchor="w", padx=10)

    def fetch_book_details(self):
        for widget in self.book_info_frame.winfo_children():
            widget.destroy()
        self.status_label.configure(text="")
        self.fetched_book_data = None
        isbn = self.isbn_entry.get()
        if len(isbn) != 13 or not isbn.isdigit():
            self.status_label.configure(text="Invalid ISBN. Please enter a 13-digit number.", text_color="red")
            return
        details = google_books.get_book_details(isbn)
        if not details:
            self.status_label.configure(text="Could not find a book with that ISBN.", text_color="red")
            return
        self.fetched_book_data = {"isbn": isbn, **details}
        ctk.CTkLabel(self.book_info_frame, text=f"Title: {details['title']}").pack()
        ctk.CTkLabel(self.book_info_frame, text=f"Author: {details['author']}").pack()
        if details['cover_url']:
            try:
                with urllib.request.urlopen(details['cover_url']) as url:
                    image_data = url.read()
                image = Image.open(io.BytesIO(image_data))
                cover_image = ctk.CTkImage(light_image=image, dark_image=image, size=(128, 192))
                ctk.CTkLabel(self.book_info_frame, image=cover_image, text="").pack(pady=10)
            except:
                ctk.CTkLabel(self.book_info_frame, text="(Cover image not available)").pack()
        ctk.CTkButton(self.book_info_frame, text="Confirm & Add to Library", command=self.add_book_to_db, fg_color="green").pack(pady=10)

    def add_book_to_db(self):
        if not self.fetched_book_data:
            self.status_label.configure(text="Please fetch a book's details first.", text_color="red")
            return
        
        # Call the database function to save the book
        data = self.fetched_book_data
        result = database.add_new_book(data['isbn'], data['title'], data['author'], data.get('cover_url', ''))
        self.status_label.configure(text=result, text_color="green" if "Success" in result else "red")
        
        # Clean up the screen after adding the book
        for widget in self.book_info_frame.winfo_children():
            widget.destroy()
        self.fetched_book_data = None

    def issue_book(self):
        isbn = self.issue_isbn_entry.get()
        student = self.student_name_entry.get()
        if not isbn or not student:
            self.issue_status_label.configure(text="Please fill in both ISBN and Student Name.", text_color="red")
            return
        result = database.issue_a_book(isbn, student)
        self.issue_status_label.configure(text=result, text_color="green" if "Success" in result else "red")

    def return_book(self):
        isbn = self.issue_isbn_entry.get()
        if not isbn:
            self.issue_status_label.configure(text="Please enter the ISBN of the book to return.", text_color="red")
            return
        result = database.return_a_book(isbn)
        self.issue_status_label.configure(text=result, text_color="green" if "Success" in result else "red")

# Entry point of the program
if __name__ == "__main__":
    database.create_database()
    app = App()
    app.mainloop()