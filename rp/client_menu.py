#!/usr/bin/env python3

from consolemenu import *
from consolemenu.items import *
from authentication import Authentication
from faceid import FaceID


class Menu():
    def __init__(self):
        self.authentication = Authentication()
        self.menu = ConsoleMenu("Library Management System", "Reception")
        self.user = None
        self.faceid = FaceID()
        function_item_login = FunctionItem("Login", self.login)
        function_item_faceid = FunctionItem("Face-ID Login", self.login_faceid)
        function_item_register = FunctionItem("Register", self.register)
        self.menu.append_item(function_item_login)
        self.menu.append_item(function_item_faceid)
        self.menu.append_item(function_item_register)


        self.menu.show()




    def register(self):
        while True:
            username = input("Username (or q! to quit): ")

            if username == 'q!':
                return

            if not self.authentication.search_user(username):
                break
            else:
                print("** Username already in use, please try again **")

        firstname = input("First name: ")
        lastname = input("Last name: ")
        email = input("Email Address: ")
        password = input("Password: ")

        self.faceid.register_user(username)

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

            if self.authentication.search_user(username):
                if self.authentication.login(username, password):
                    self.user = self.authentication.get_user(username)
                    print("Welcome " + self.user.getFirstname())
                    break
                else:
                    attempts += 1
                    print("Login Invalid!")
            else:
                print("Login Invalid!")

    def login_faceid(self):
        username = self.faceid.recognize_user()

        if username == "Unknown":
            print("Login Failed")
            return
        else:
            self.user = self.authentication.get_user(username)
            print(self.user.getFirstname)




if __name__ == "__main__":
    reception = Menu()
