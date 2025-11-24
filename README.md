# Library Management
A simple library management app. Books can be added to your collection simply by entering an ISBN. The app automatically fetches the title, author, and cover image using the Google Books API. It allows you to track book loans and view the status of your entire inventory in a clean, visual layout.

## Overview of the project

This is little desktop app was to created to be a simple and minimalistic tool which helps small library manage its books. Instead of using a boring spreadsheet, this app provides a nice graphical interface to add books, issue them to students, and see what's available at a glance. The coolest feature is that you only need the book's ISBN number! The app then connects to the Google Books API to automatically grab the book's title, author, and even its cover image.

##  Features

*   **Add New Books via ISBN:** Just type in the 13-digit ISBN and the app fetches all the details for you.
*   **Visual Confirmation:** See the book's cover and details before you add it to your library.
*   **Issue & Return Books:** Easily track which books have been borrowed and by whom.
*   **View Your Collection:** See a simple, clean list of all the books in your library and their status (Available/Issued).
*   **Track Borrowed Books:** Get a separate view of all the books that are currently checked out.

##  Technologies Used

*   **Python:** The core language for the application.
*   **CustomTkinter:** For creating the modern graphical user interface (GUI).
*   **Pillow (PIL):** Used to handle and display the book cover images in the app.
*   **SQLite:** For the database, which is all stored in a single `library.db` file. No complicated setup needed!
*   **Google Books API:** To fetch book information from the internet.

##  How to Get Started

To run this project on your own computer, follow these simple steps.

**1. Clone the repository:**
```bash
git clone https://github.com/Qwerrty-uiop/library-management
cd library-management
```

**2. Install the necessary libraries:**
Make sure you have Python 3 installed. Then, run this command in your terminal:```bash
pip install -r requirements.txt
```

**3. Run the application:**
```bash
python app.py
```
And that's all.

##  Instructions for Testing

Test Case 1: Adding a New Book
1. Launch the application. You will start on the "Add Book" screen.
2. In the ISBN entry box, type 9780345339683 and click the "Fetch Book Info" button.
3. Expected Result: The book's title ("The Hobbit"), author, and cover image should appear. A green "Confirm & Add to Library" button will also appear.
4. Click the "Confirm & Add to Library" button.
5. Expected Result: You should see a "Success!" message.
6. Navigate to the "View All Books" tab.
7. Expected Result: You should see "The Hobbit" listed with a status of "Available."

Test Case 2: Handling a Duplicate Book
1. Navigate back to the "Add Book" tab.
2. Enter the same ISBN, 9780345339683, and click "Fetch Book Info" again.
3. Click the "Confirm & Add to Library" button.
4. Expected Result: The app should display an error message indicating that a book with this ISBN already exists.

Test Case 3: Issuing and Returning a Book
1. Navigate to the "Issue/Return" tab.
2. In the "Enter Book ISBN" box, type.
3. In the "Enter Student Name" box, type a name (e.g., "John Doe").
4. Click the "Issue Book" button.
5. Expected Result: A success message should appear.
6. To verify, navigate to the "View Issued Books" tab. You should see "The Hobbit" listed as issued to "John Doe."
7. Now, navigate back to the "Issue/Return" tab.
8. Ensure the ISBN 9780345339683 is still in the box and click the "Return Book" button.
9. Expected Result: A success message for the return should appear.
10. To verify, go to the "View Issued Books" tab again. It should now be empty. Then, check the "View All Books" tab; the status of "The Hobbit" should be back to "Available."

Test Case 4: Handling Invalid Input
1. Go to the "Add Book" tab.
2. Enter an invalid ISBN, such as 12345.
3. Click "Fetch Book Info".
4. Expected Result: The app should display an error message about an invalid ISBN and should not proceed.

## 📸 Screenshots

**Add a New Book Window**
<img width="1589" height="1236" alt="Screenshot 2025-11-25 003739" src="https://github.com/user-attachments/assets/cdf956af-e4ca-400c-8ab7-eca525d53f51" />

**Issue or Return Book Window**
<img width="1596" height="1248" alt="Screenshot 2025-11-25 003757" src="https://github.com/user-attachments/assets/d0ca00e3-8ca6-49f9-bc8e-0e11be668af6" />

**All Books in the Library Window**
<img width="1592" height="1246" alt="Screenshot 2025-11-25 004147" src="https://github.com/user-attachments/assets/5854a765-3caf-468e-9bea-cfb87a4b9cd9" />

**Currently Issued Books**
<img width="1592" height="1250" alt="Screenshot 2025-11-25 004200" src="https://github.com/user-attachments/assets/59ec9f37-ba60-4a8b-ae28-00136b1c43aa" />
