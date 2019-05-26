import sqlite3
import os

class Database:
    """
    Database abstraction class for handling all access to Database.
    """
    def __init__(self):
        """
        This function intialises the database, sets a flag for determining if the database is connected or not, and then the connect method is executed.
        """
        # Initialise database filename
        self.database = 'user.db'
        # Set a flag for determining if database is connected or not
        self.connected = False
        # Execute the connect method
        self.connect()

    def connect(self):
        """
        This function establishes a connection to an SQLite database. If file doesn't exist it will be created. Detect_types is used for mapping Python types to database types.
        """
        # Establish a connection to an sqlite database. It file doesn't exist it will be created
        # detect_types is used for mapping python types to database types. Handy but not required
        self.connection = sqlite3.connect(self.database, check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES)

        # Store a cursor variable pointing to the sqlite cursor
        self.cursor = self.connection.cursor()
        # Set connection flag to true
        self.connected = True

    def close(self):
        """
        This function commits database changes, closes the connection and sets the connection flag to false.
        """
        # Commit database changes, close connection and set connection flag to false
        self.connection.commit()
        self.connection.close()
        self.connected = False

    def add_user(self, username: str, firstname: str, lastname: str, email: str, password: str):
        """
        This function will add a user to the database.
        """
        self.check_create_user_table()

        if not self.connected:
            self.connect()

        self.cursor.execute("""INSERT INTO user(username, first_name, last_name, email, password)
                            VALUES (:username, :first_name, :last_name, :email, :password)""",
                            {"username": username, "first_name": firstname, "last_name": lastname, "email": email, "password": password})
        self.close()

    def check_create_user_table(self):
        """
        This function will check if a user table has been created. If not, create the table.
        """
        if not self.connected:
            self.connect()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(username TEXT PRIMARY KEY,
                            first_name TEXT NOT NULL, last_name TEXT NOT NULL, 
                            email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)""")
        self.close()
    
    def check_user(self, username: str):
        """
        This function gets and checks if a certain username
        exists in the User table, before they are 
        connected.
        """
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
        """
        This function gets the password for
        a specific user from the User
        table.
        """
        self.check_create_user_table()

        if not self.connected:
            self.connect()

        self.cursor.execute("""SELECT password FROM user WHERE username = :username""",
                            {"username": username})

        for row in self.cursor:
            password = row[0]

        self.close()

        return password

    def find_user(self, username: str):
        """
        This function will find a user in the smart library database.
        """
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
