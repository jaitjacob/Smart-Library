
class ServerUser:
    def __init__(self, lmsuserid: int, username: str, name: str):
        self.lmsuserid = lmsuserid
        self.username = username
        self.name = name

    def get_lmsuserid(self):
        return self.lmsuserid

    def get_username(self):
        return self.username

    def get_name(self):
        return self.name
