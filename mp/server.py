from clouddb import CloudDB
from server_user import ServerUser


class Server:
    def __init__(self, username: str):
        self.clouddb = CloudDB()
        self.user = self.get_user(username)

    def get_user(self, username: str):
        rows = self.clouddb.get_lmsuser(username)

        for row in rows:
            return ServerUser(row[0], row[1], row[2])

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
        if self.clouddb.check_book(bookid):
            self.clouddb.borrow_book(self.user.get_lmsuserid(), bookid)
            return True
        else:
            return False
