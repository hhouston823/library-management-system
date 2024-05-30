class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def __str__(self):
        return f"Name: {self.__name}, Description: {self.__description}, Category: {self.__category}"
