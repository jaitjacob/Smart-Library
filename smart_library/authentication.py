#import bcrypt
#from rp.database import Database
#from user import User

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
        This function handles the user logging into the system, taking in the arguments
        of the user's username and their password.
        """
        self.database.find_user(username)

    def create_user(self, username: str, firstname: str, lastname: str, email: str, password: str):
        """
        This function handles the creation of a new user of the system, taking in the arguments
        of the username, firstname, lastname, email and password that the user enters.
        """
        self.database.add_user(username, firstname, lastname, email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)))

    def get_user(self, get_username):
        """
        This function handles getting and returning a user via their unique username on the system.
        """
        username, first_name, last_name, email, password = self.database.get_user(get_username)

        user = User(username, password, first_name, last_name, email)

        return user

    def search_user(self, username):
        """
        This function handles finding a user within the database, who
        has already registered with the system previously.
        """
        return self.database.find_user(username)
