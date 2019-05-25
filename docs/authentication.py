import bcrypt
from rp.database import Database


class Authentication:
    def __init__(self):
        self.database = Database()

    def login(self, username: str, password: str):
        self.database.find_user(username)

    def create_user(self, username: str, firstname: str, lastname: str, email: str, password: str):
        self.database.add_user(username, firstname, lastname, email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)))

    def search_user(self, username):
        return self.database.find_user(username)
