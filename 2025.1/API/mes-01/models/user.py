import bcrypt

class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = User.get_hash_password(password)

    @staticmethod
    def get_hash_password(password: str):
       salt = bcrypt.gensalt()
       hashed = bcrypt.hashpw(password.encode(), salt)
       return hashed

    def to_dict(self):
       return {'user': self.login}
