

class User:
    def __init__(self, username: str, password: str, firstname: str, lastname: str, email: str):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def getEmail(self):
        return self.email
