import sqlite3
import os


# Database abstraction class for handling all access to Database
class Database:
    def __init__(self):
        # Initialise database filename
        self.database = 'user.db'
        # Set a flag for determining if database is connected or not
        self.connected = False
        # Execute the connect method
        self.connect()

    def connect(self):
        # Establish a connection to an sqlite database. It file doesn't exist it will be created
        # detect_types is used for mapping python types to database types. Handy but not required
        self.connection = sqlite3.connect(self.database, check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES)

        # Store a cursor variable pointing to the sqlite cursor
        self.cursor = self.connection.cursor()
        # Set connection flag to true
        self.connected = True

    def close(self):
        # Commit database changes, close connection and set connection flag to false
        self.connection.commit()
        self.connection.close()
        self.connected = False

    def add_user(self, username: str, firstname: str, lastname: str, email: str, password: str):
        self.check_create_user_table()

        if not self.connected:
            self.connect()

        self.cursor.execute("""INSERT INTO user(username, first_name, last_name, email, password)
                            VALUES (:username, :first_name, :last_name, :email, :password)""",
                            {"username": username, "first_name": firstname, "last_name": lastname, "email": email, "password": password})
        self.close()

    def check_create_user_table(self):
        if not self.connected:
            self.connect()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(username TEXT PRIMARY KEY,
                            first_name TEXT NOT NULL, last_name TEXT NOT NULL, 
                            email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)""")
        self.close()

    def check_user(self, username: str):
        self.check_create_user_table()

        if not self.connected:
            self.connect()

        self.cursor.execute("""SELECT COUNT(username) FROM user WHERE username = :username""",
                            {"username": username})
        for row in self.cursor:
            if row[0] == 1:
                found = True
            else:
                found = False

        self.close()

        return found

    def get_password(self, username: str):
        self.check_create_user_table()

        if not self.connected:
            self.connect()

        self.cursor.execute("""SELECT password FROM user WHERE username = :username""",
                            {"username": username})

        for row in self.cursor:
            password = row[0]

        self.close()

        return password

    def get_user(self, username: str):
        self.check_create_user_table()

        if not self.connected:
            self.connect()

        self.cursor.execute("""SELECT * FROM user WHERE username = :username""",
                            {"username": username})
        for row in self.cursor:
            username = row[0]
            first_name = row[1]
            last_name = row[2]
            email = row[3]
            password = row[4]

        self.close()

        return username, first_name, last_name, email, password

