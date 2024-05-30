# Library Management System

## Overview

The Library Management System is a command-line-based application designed to streamline the management of books and resources within a library. This system allows users to browse, borrow, return, and explore a collection of books. The application demonstrates Object-Oriented Programming (OOP) principles, including encapsulation, inheritance, polymorphism, and modularity.

## Features

- **Book Operations**:
  - Add a new book
  - Borrow a book
  - Return a book
  - Search for a book by ISBN or title
  - Display all books

- **User Operations**:
  - Add a new user
  - View user details
  - Display all users

- **Author Operations**:
  - Add a new author
  - View author details
  - Display all authors

- **Genre Operations**:
  - Add a new genre
  - View genre details
  - Display all genres

## Class Structure

- **Book**: Represents individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
- **User**: Represents library users with attributes like name, library ID, and a list of borrowed book titles.
- **Author**: Represents book authors with attributes like name and biography.
- **Genre**: Represents book genres with attributes like name, description, and category.

Specialized book categories using inheritance:
- **FictionBook**
- **NonFictionBook**

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. **Ensure Python is installed** (Python 3.6 or higher).

## Usage

1. **Navigate to the project directory**:
    ```sh
    cd library-management-system
    ```

2. **Run the application**:
    ```sh
    python library_management_system.py
    ```

3. **Follow the on-screen instructions** to interact with the Library Management System.

## Code Structure

- **library_management_system.py**: Main script containing the `LibraryManagementSystem` class and the user interface.
- **book.py**: Contains the `Book`, `FictionBook`, and `NonFictionBook` classes.
- **user.py**: Contains the `User` class.
- **author.py**: Contains the `Author` class.
- **genre.py**: Contains the `Genre` class.

## Input Validation

- ISBN must be 13 digits.
- Publication date must follow the format `YYYY-MM-DD`.
- Book type must be either 'f' (Fiction) or 'n' (Non-Fiction).

## Error Handling

- Graceful error handling using `try`, `except`, `else`, and `finally` blocks to manage potential issues such as incorrect user input or file operations.
