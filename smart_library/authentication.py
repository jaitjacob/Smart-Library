import bcrypt
from rp.database import Database


class Authentication:
    """
    Authentication class handles clients logging into the system and gaining access to the application.
    """
    def __init__(self):
        """
        This function initalises the database.
        """
        self.database = Database()

    def login(self, username: str, password: str):
        """
        This function handles the user logging into the system.
        """
        self.database.find_user(username)

    def create_user(self, username: str, firstname: str, lastname: str, email: str, password: str):
        """
        This function handles the creation of a new user of the system.
        """
        self.database.add_user(username, firstname, lastname, email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)))

    def search_user(self, username):
        """
        This function handles the finding of a user within the database, who
        has already registered with the system previously.
        """
        return self.database.find_user(username)
