import bcrypt
from database import Database

database = Database()

database.add_user("bhan", "Brian", "Han", "a@b.com", bcrypt.hashpw("password".encode('utf-8'), bcrypt.gensalt(12)))


