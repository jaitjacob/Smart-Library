#!/usr/bin/env python3

from consolemenu import *
from consolemenu.items import *
from authentication import Authentication


class Menu():
    def __init__(self):
        self.authentication = Authentication()
        self.menu = ConsoleMenu("Library Management System", "Reception")

        function_item_login = FunctionItem("Login", self.login)
        function_item_register = FunctionItem("Register", self.register)
        self.menu.append_item(function_item_login)
        self.menu.append_item(function_item_register)

        self.menu.show()

    def register(self):
        while True:
            username = input("Username: ")

            if not self.authentication.search_user(username):
                break
            else:
                print("** Username already in use, please try again **")

        firstname = input("First name: ")
        lastname = input("Last name: ")
        email = input("Email Address: ")
        password = input("Password: ")
        print("You have successfully registered")

        self.authentication.create_user(username, firstname, lastname, email, password)

    def login(self):
        attempts = 0
        while True:
            if attempts == 3:
                print("Too many failed attempts.")
                break
            username = input("Username: ")
            password = input("Password: ")

            if self.authentication.login(username, password):
                print("You have successfully logged in")
                break
            else:
                attempts +=1
                print("Login Invalid!")





if __name__ == "__main__":
    reception = Menu()
