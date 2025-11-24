# Project Statement: Library Database Management System

## Problem Statement

Small community or school libraries often manage their book collections with manual methods like paper ledgers or basic spreadsheets. These methods are time-consuming to update with higher chances of error, and makes it difficult to quickly track which books are available or who has borrowed them. There is a need for a simple, low-cost digital solution that is simple to use for non-technical users and automates the process of cataloging and tracking books.

## Scope of the Project

The goal of this project is to develop a desktop application that addresses the needs of a small library and simplifies the task of managing the log of book issues.

**In Scope:**
*   A user-friendly graphical interface for all interactions.
*   A feature to add new books to the database using only their ISBN. The system will auto add the title and author.
*   The ability to perform basic CRUD (Create, Read, Update, Delete) operations on the book records. In this project, this is implemented as Add, View, Issue, and Return functions.
*   A system to track the issue and return of books to individuals.
*   Storing all data in a local SQLite database file.

**Out of Scope:**
*   User accounts or login systems for library members (the app is designed to be used by one librarian/manager).
*   A web-based interface or online access for library members.
*   Advanced features like managing book reservations, handling fines for overdue books, or generating complex analytical reports.

## Target Users

The primary target user is a **librarian or a volunteer** at a small-scale library. This could include:
*   A school library.
*   A small community center library.
*   A library within a company or office.
*   An individual with a large personal book collection they want to manage.

The user is expected to have basic computer skills but is not required to be a tech expert.

## High-Level Features

The system is built around three major functional modules that create a logical workflow for the user:

1.  **Book Cataloging Module:**
    *   Allows the user to add new books to the library's database.
    *   Uses the Google Books API to minimize manual data entry, requiring only an ISBN.

2.  **Management Module:**
    *   Enables the librarian to issue a book to a specific person (e.g., a student).
    *   Allows the librarian to process the return of a book, making it available again.

3.  **Viewing & Reporting Module:**
    *   Provides a view of all books currently in the library collection, along with their status.
    *   Offers a separate view to quickly see all books that are currently issued and to whom.
