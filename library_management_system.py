from database import connect_to_database

import re
from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author
from genre import Genre

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def display_main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")

            choice = input("Please select an option (1-5): ")
            
            if choice == '1':
                self.book_operations_menu()
            elif choice == '2':
                self.user_operations_menu()
            elif choice == '3':
                self.author_operations_menu()
            elif choice == '4':
                self.genre_operations_menu()
            elif choice == '5':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations_menu(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            self.add_book()
        elif choice == '2':
            self.borrow_book()
        elif choice == '3':
            self.return_book()
        elif choice == '4':
            self.search_book()
        elif choice == '5':
            self.display_all_books()
        else:
            print("Invalid choice. Please try again.")

    def user_operations_menu(self):
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            self.add_user()
        elif choice == '2':
            self.view_user_details()
        elif choice == '3':
            self.display_all_users()
        else:
            print("Invalid choice. Please try again.")

    def author_operations_menu(self):
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            self.add_author()
        elif choice == '2':
            self.view_author_details()
        elif choice == '3':
            self.display_all_authors()
        else:
            print("Invalid choice. Please try again.")

    def genre_operations_menu(self):
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            self.add_genre()
        elif choice == '2':
            self.view_genre_details()
        elif choice == '3':
            self.display_all_genres()
        else:
            print("Invalid choice. Please try again.")

    def add_book(self):
        try:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book (13 digits): ")
            if not re.match(r'^\d{13}$', isbn):
                raise ValueError("Invalid ISBN format. ISBN should be 13 digits.")
            genre = input("Enter the genre of the book: ")
            publication_date = input("Enter the publication date (YYYY-MM-DD): ")
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', publication_date):
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
            book_type = input("Is this a Fiction or Non-Fiction book? (f/n): ").strip().lower()
            if book_type == 'f':
                sub_genre = input("Enter the sub-genre of the book: ")
                new_book = FictionBook(title, author, isbn, genre, publication_date, sub_genre)
            elif book_type == 'n':
                field = input("Enter the field of the book: ")
                new_book = NonFictionBook(title, author, isbn, genre, publication_date, field)
            else:
                raise ValueError("Invalid book type. Enter 'f' for Fiction or 'n' for Non-Fiction.")
            
            self.books.append(new_book)
            print(f"Book '{title}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Book Operations menu...")

    def borrow_book(self):
        try:
            isbn = input("Enter the ISBN of the book to borrow: ")
            for book in self.books:
                if book.get_isbn() == isbn:
                    if book.borrow():
                        print(f"You have successfully borrowed '{book.get_title()}'.")
                    else:
                        print(f"Sorry, the book '{book.get_title()}' is currently unavailable.")
                    return
            print("Book not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Book Operations menu...")

    def return_book(self):
        try:
            isbn = input("Enter the ISBN of the book to return: ")
            for book in self.books:
                if book.get_isbn() == isbn:
                    book.return_book()
                    print(f"You have successfully returned '{book.get_title()}'.")
                    return
            print("Book not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Book Operations menu...")

    def search_book(self):
        try:
            search_term = input("Enter the ISBN or title of the book to search: ")
            for book in self.books:
                if book.get_isbn() == search_term or book.get_title().lower() == search_term.lower():
                    print(book)
                    return
            print("Book not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Book Operations menu...")

    def display_all_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")
        input("Press Enter to return to the Book Operations menu...")

    def add_user(self):
        try:
            name = input("Enter the name of the user: ")
            library_id = input("Enter the library ID of the user: ")
            new_user = User(name, library_id)
            self.users.append(new_user)
            print(f"User '{name}' added successfully.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the User Operations menu...")

    def view_user_details(self):
        try:
            library_id = input("Enter the library ID of the user to view: ")
            for user in self.users:
                if user.get_library_id() == library_id:
                    print(user)
                    return
            print("User not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the User Operations menu...")

    def display_all_users(self):
        if self.users:
            for user in self.users:
                print(user)
        else:
            print("No users in the library.")
        input("Press Enter to return to the User Operations menu...")

    def add_author(self):
        try:
            name = input("Enter the name of the author: ")
            biography = input("Enter the biography of the author: ")
            new_author = Author(name, biography)
            self.authors.append(new_author)
            print(f"Author '{name}' added successfully.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Author Operations menu...")

    def view_author_details(self):
        try:
            name = input("Enter the name of the author to view: ")
            for author in self.authors:
                if author.get_name().lower() == name.lower():
                    print(author)
                    return
            print("Author not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Author Operations menu...")

    def display_all_authors(self):
        if self.authors:
            for author in self.authors:
                print(author)
        else:
            print("No authors in the library.")
        input("Press Enter to return to the Author Operations menu...")

    def add_genre(self):
        try:
            name = input("Enter the name of the genre: ")
            description = input("Enter the description of the genre: ")
            category = input("Enter the category of the genre: ")
            new_genre = Genre(name, description, category)
            self.genres.append(new_genre)
            print(f"Genre '{name}' added successfully.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Genre Operations menu...")

    def view_genre_details(self):
        try:
            name = input("Enter the name of the genre to view: ")
            for genre in self.genres:
                if genre.get_name().lower() == name.lower():
                    print(genre)
                    return
            print("Genre not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            input("Press Enter to return to the Genre Operations menu...")

    def display_all_genres(self):
        if self.genres:
            for genre in self.genres:
                print(genre)
        else:
            print("No genres in the library.")
        input("Press Enter to return to the Genre Operations menu...")

# Example usage
if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.display_main_menu()
