import MySQLdb
from datetime import datetime


class CloudDB:
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
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def search_available(self, title: str, author: str):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE BookID NOT IN ( "
                           "SELECT DISTINCT BookID FROM BookBorrowed "
                           "WHERE Status='borrowed' ) "
                           "AND Title LIKE %s "
                           "AND Author LIKE %s ", ('%' + title + '%', '%' + author + '%'))
            return cursor.fetchall()

    def list_titles(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book ")
            return cursor.fetchall()

    def borrow_book(self, userid: int, bookid: int ):
        # Return the book in case it was already borrowed and hadn't been properly returned
        self.return_book(bookid)

        borrowdate = datetime.today()

        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO BookBorrowed (LmsUserID, BookID, Status, BorrowedDate) "
                           "VALUES (%s, %s, %s, %s)", (userid, bookid, 'borrowed', borrowdate.strftime("%Y-%m-%d")))
            self.connection.commit()

            return cursor.rowcount == 1

    def return_book(self, bookid: int):
        returndate = datetime.today()

        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE BookBorrowed "
                           "SET Status = %s, ReturnedDate = %s "
                           "WHERE BookID = %s AND Status = 'borrowed'", ('returned', returndate.strftime("%Y-%m-%d"), bookid))
            self.connection.commit()

            return cursor.rowcount == 1

    def add_lmsuser(self, username: str, name: str):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO LmsUser (UserName, Name) "
                           "VALUES (%s, %s)", (username, name))
            self.connection.commit()

            return cursor.rowcount == 1

    def get_lmsuser(self, username):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book "
                           "WHERE UserName = %s", (username))
            return cursor.fetchall()


db = CloudDB()

db.add_lmsuser("bhan", "Brian")

for row in db.get_lmsuser("bhan"):
    print(row)
