class User:
    """ 
    This class refers simply to the details of a user. The arguments taken
    for this class include the user's username, password, firstname, lastname
    and email.
    """
    def __init__(self, username: str, password: str, firstname: str, lastname: str, email: str):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def getUsername(self):
        """Get and return the username of a user."""
        return self.username

    def getPassword(self):
       	"""Get and return the password of a user."""
        return self.password

    def getFirstname(self):
        """Get and return the firstname of a user."""
        return self.firstname

    def getLastname(self):
        """Get and return the lastname of a user."""
        return self.lastname

    def getEmail(self):
        """Get and return the email of a user."""
        return self.email

