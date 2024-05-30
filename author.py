class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_biography(self):
        return self.__biography

    def set_biography(self, biography):
        self.__biography = biography

    def __str__(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
