from consolemenu import *
from consolemenu.items import *
from server import Server


class ServerMenu:
    def __init__(self, username: str):
        self.server = Server(username)
        self.menu = ConsoleMenu("Library Management System", "Master")
        function_item_search = FunctionItem("Search a book", self.search_book)
        function_item_borrow = FunctionItem("Borrow a book", self.borrow_book)
        function_item_return = FunctionItem("Return a book", self.return_book)
        function_item_logout = FunctionItem("Logout", self.logout)

        self.menu.append_item(function_item_search)
        self.menu.append_item(function_item_borrow)
        self.menu.append_item(function_item_return)
        self.menu.append_item(function_item_logout)

        self.menu.show()

    def search_book(self):
        title = input("Title contains: ")
        author = input("Author contains: ")

        bookids, titles, authors, publisheddates = self.server.search_book(title, author)

        headers = ['Book ID', 'Title', 'Author', 'Published Date']

        data = [headers] + list(zip(bookids, titles, authors, publisheddates))

        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(12) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))

    def borrow_book(self):
        print("To be implemented")

    def return_book(self):
        print("To be implemented")

    def logout(self):
        print("To be implemented")


