class ServerUser:
    """
    This class deals with a user on the library server, taking in the arguments
    of their user id on the system, their username and their actual name.
    """
    def __init__(self, lmsuserid: int, username: str, name: str):
        self.lmsuserid = lmsuserid
        self.username = username
        self.name = name

    def get_lmsuserid(self):
        """Gets and returns the user id of a library user."""
        return self.lmsuserid

    def get_username(self):
        """Gets and returns the username of a library user."""
        return self.username

    def get_name(self):
        """Gets and returns the actual name of a library user."""
        return self.name
