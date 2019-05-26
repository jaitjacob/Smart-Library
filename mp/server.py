from clouddb import CloudDB
from server_user import ServerUser


class Server:
    def __init__(self, username: str):
        self.clouddb = CloudDB()
        self.user = self.find_user(username)

    def find_user(self, username: str):
        rows = self.clouddb.get_lmsuser(username)

        for row in rows:
            return ServerUser(row[0], row[1], row[2])

    def get_user(self):
        return self.user

    def search_book(self, title: str, author: str):

        rows = self.clouddb.search_available(title, author)

        bookids = []
        titles = []
        authors = []
        publisheddates =[]

        for row in rows:
            bookids.append(row[0])
            titles.append(row[1])
            authors.append(row[2])
            publisheddates.append(row[3])

        return bookids, titles, authors, publisheddates

    def borrow_book(self, bookid: int):
        # Check if the book is available to borrow
        if self.clouddb.check_book(bookid):
            self.clouddb.borrow_book(self.user.get_lmsuserid(), bookid)
            return True
        else:
            return False

    def return_book(self, bookid: int):
        # Check if the book is available to borrow, if so, it cannot be returned
        if self.clouddb.check_book(bookid):
            return False
        else:
            self.clouddb.return_book(bookid)
            return True
