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
        borrowdate = datetime.today()

        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO BookBorrowed (LmsUserID, BookID, Status, BorrowedDate)"
                           "VALUES (%s, %s, %s, %s", (userid, bookid, 'borrowed', borrowdate.strftime("%Y-%m-%d")))
            return cursor.fetchall()

    def return_book(self, bookid: int):
        returndate = datetime.today()

        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE "
                           "SET Status = %s, ReturnedDate %s "
                           "WHERE BookID = %s", ('returned', returndate.strftime("%Y-%m-%d"), bookid))
            return cursor.fetchall()




db = CloudDB()

for row in db.search_available("Transmission", "", ""):
    print(row)
