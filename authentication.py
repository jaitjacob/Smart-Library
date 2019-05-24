import bcrypt
from database import Database
from user import User


class Authentication:
    def __init__(self):
        self.database = Database()

    def login(self, username: str, password: str):
        hashed_password = self.database.get_password(username)
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    def create_user(self, username: str, firstname: str, lastname: str, email: str, password: str):
        self.database.add_user(username, firstname, lastname, email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)))

    def search_user(self, username):
        return self.database.check_user(username)

    def get_user(self, get_username):
        username, first_name, last_name, email, password = self.database.get_user(get_username)

        user = User(username, password, first_name, last_name, email)

        return user