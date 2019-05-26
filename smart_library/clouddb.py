#import MySQLdb
#from datetime import datetime


class CloudDB:
    """ This class handles the actions that take place in the Google Cloud Database."""
    HOST = "35.197.161.11"
    USER = "root"
    PASSWORD = "468yANs7gktk5DdL"
    DATABASE = "lms"

    def __init__(self, connection=None):
        if (connection == None):
            connection = MySQLdb.connect(CloudDB.HOST, CloudDB.USER,
                                         CloudDB.PASSWORD, CloudDB.DATABASE)
        self.connection = connection

    def close(self):
        """This method closses the database connection."""
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def check_book(self, bookid: int):
        """Checks via an SQL query if a certain book is available in the library."""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * "
                           "FROM BookBorrowed "
                           "WHERE BookID = %s AND Status = 'borrowed'", (bookid, ))

            return cursor.rowcount == 0


    def search_available(self, title: str, author: str):
        """Searches via an SQL query for a title and author within the library collection."""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE BookID NOT IN ( "
                           "SELECT DISTINCT BookID FROM BookBorrowed "
                           "WHERE Status='borrowed' ) "
                           "AND Title LIKE %s "
                           "AND Author LIKE %s ", ('%' + title + '%', '%' + author + '%'))
            return cursor.fetchall()

    def list_titles(self):
        """Lists all titles via an SQL query."""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book ")
            return cursor.fetchall()

    def get_book(self, bookid: int):
        """Gets a book with a certain book ID that is passed through as an argument."""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book "
                           "WHERE BookID = %s", (bookid, ))
            return cursor.fetchall()

    def borrow_book(self, userid: int, bookid: int ):
        """Borrow a book with a certain id that will be assigned to a user with their own unique id."""
        # Return the book in case it was already borrowed and hadn't been properly returned
        self.return_book(bookid)

        borrowdate = datetime.today()

        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO BookBorrowed (LmsUserID, BookID, Status, BorrowedDate) "
                           "VALUES (%s, %s, %s, %s)", (userid, bookid, 'borrowed', borrowdate.strftime("%Y-%m-%d")))
            self.connection.commit()

            return cursor.rowcount == 1

    def return_book(self, bookid: int):
        """Return a book with a certain book ID that is passed through as an argument."""
        returndate = datetime.today()

        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE BookBorrowed "
                           "SET Status = %s, ReturnedDate = %s "
                           "WHERE BookID = %s AND Status = 'borrowed'", ('returned', returndate.strftime("%Y-%m-%d"), bookid))
            self.connection.commit()

            return cursor.rowcount == 1

    def add_lmsuser(self, username: str, name: str):
        """Add a library user that takes the arguments of username for user when they are logged in, and their actual name.""" 
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO LmsUser (UserName, Name) "
                           "VALUES (%s, %s)", (username, name))
            self.connection.commit()

            return cursor.rowcount == 1

    def get_lmsuser(self, username):
        """Get a library user that takes the argument of username for user when they are logged in."""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM LmsUser "
                           "WHERE UserName = %s", (username, ))
            return cursor.fetchall()

