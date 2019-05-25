import MySQLdb


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

    def search_available(self, title: str, author: str, date: str):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE BookID NOT IN ( "
                           "SELECT DISTINCT BookID FROM BookBorrowed "
                           "WHERE Status='borrowed' ) "
                           "AND Title LIKE %s",
				('%' + title + '%',))
            return cursor.fetchall()

    def list_titles(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book ")
            return cursor.fetchall()


db = CloudDB()

for row in db.search_available("Transmission", " ", " "):
    print(row)
