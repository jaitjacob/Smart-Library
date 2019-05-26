from consolemenu import *
from consolemenu.items import *
from server import Server
from server_user import ServerUser


class ServerMenu:
    def __init__(self, username: str):
        self.server = Server(username)
        self.menu = ConsoleMenu("Library Management System - " + self.server.get_user().get_name(), "Master")
        function_item_search = FunctionItem("Search a book", self.search_book)
        function_item_borrow = FunctionItem("Borrow a book", self.borrow_book)
        function_item_return = FunctionItem("Return a book", self.return_book)

        self.menu.append_item(function_item_search)
        self.menu.append_item(function_item_borrow)
        self.menu.append_item(function_item_return)

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

        input("Press any key to return to the main menu")

    def borrow_book(self):
        bookid = input("Please enter the book id you wish to borrow: ")

        if self.server.borrow_book(bookid):
            print("Book succesfully borrowed")
        else:
            print("Book already borrowed, please return first")

        input("Press any key to return to the main menu")

    def return_book(self):
        bookid = input("Please enter the book id you wish to return: ")

        if self.server.return_book(bookid):
            print("Book succesfully returned")
        else:
            print("Book not borrowed, please borrow first")

        input("Press any key to return to the main menu")

    def logout(self):
        print("To be implemented")


if __name__ == "__main__":
    master = ServerMenu('bhan')
