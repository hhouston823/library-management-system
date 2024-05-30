class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    # Getters and Setters
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Publication Date: {self.__publication_date}, Available: {self.__is_available}"


class FictionBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, sub_genre):
        super().__init__(title, author, isbn, genre, publication_date)
        self.__sub_genre = sub_genre

    def get_sub_genre(self):
        return self.__sub_genre

    def set_sub_genre(self, sub_genre):
        self.__sub_genre = sub_genre

    def __str__(self):
        return f"{super().__str__()}, Sub-genre: {self.__sub_genre}"


class NonFictionBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, field):
        super().__init__(title, author, isbn, genre, publication_date)
        self.__field = field

    def get_field(self):
        return self.__field

    def set_field(self, field):
        self.__field = field

    def __str__(self):
        return f"{super().__str__()}, Field: {self.__field}"
