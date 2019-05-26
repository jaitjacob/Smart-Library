#from clouddb import CloudDB
#from server_user import ServerUser
#from calendar import Calendar
#from book import Book


class Server:
    """This class holds all information regarding the Smart Library server."""
    def __init__(self, username: str):
        self.clouddb = CloudDB()
        self.user = self.find_user(username)
        self.calendar = Calendar()

    def find_user(self, username: str):
        """Finds a user by their unique username on the system."""
        rows = self.clouddb.get_lmsuser(username)

        for row in rows:
            return ServerUser(row[0], row[1], row[2])

    def get_user(self):
        """Gets and returns a user."""
        return self.user

    def search_book(self, title: str, author: str):
        """Searches for a book taking the arguments of title and author."""
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
        """Borrow a book referring to its ID."""
        # Check if the book is available to borrow
        if self.clouddb.check_book(bookid):
            book = self.get_book(bookid)
            self.clouddb.borrow_book(self.user.get_lmsuserid(), bookid)
            self.calendar.insert(self.user.get_lmsuserid(), book.get_bookid(), book.get_title(), book.get_author())
            return True
        else:
            return False

    def return_book(self, bookid: int):
        """Return a book referring to its ID."""
        # Check if the book is available to borrow, if so, it cannot be returned
        if self.clouddb.check_book(bookid):
            return False
        else:
            self.clouddb.return_book(bookid)
            return True

    def get_book(self, bookid: int):
        """Get and return a book taking into account its ID."""
        rows = self.clouddb.get_book(bookid)

        for row in rows:
            return Book(row[0], row[1], row[2], row[3])
