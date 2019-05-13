#!/usr/bin/env python3

#from consolemenu import *
#from consolemenu.items import *
from authentication import Authentication


class Menu():
    """
    Client menu class that handles the login and register of users.
    """
    def __init__(self):
        self.authentication = Authentication()
        self.menu = ConsoleMenu("Library Management System", "Reception")

        function_item_login = FunctionItem("Login", self.login)
        function_item_register = FunctionItem("Register", self.register)
        self.menu.append_item(function_item_login)
        self.menu.append_item(function_item_register)

        self.menu.show()

    def register(self):
        """
        This function handles the registering of a user. The user will be required to enter a username they would like to use, then the system will authenticate whether the username is available or already been taken.
        """
        while True:
            username = input("Username: ")

            if not self.authentication.search_user(username):
                break
            else:
                print("** Username already in use, please try again **")

    def login(self):
        """
        This function handles the login of a user, via authenticating their unique username.
        """
        while True:
            username = input("Username: ")

            if self.authentication.search_user(username):
                break
            else:
                print("** Username not found, please try again **")


if __name__ == "__main__":
    reception = Menu()
