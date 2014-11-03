from readhub import db
from hashlib import sha1
import uuid


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(140), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    salt = db.Column(db.String(40), nullable=False)

    def __init__(self, email, password):
        self.email = email
        salt = uuid.uuid4().hex
        self.salt = sha1(salt).hexdigest()
        self.password = sha1(password + self.salt).hexdigest()

    def __repr__(self):
        return '<User %s %s %s>' % (self.email, self.password, self.salt)

    def valid_password(self, password):
        hash = sha1(password + self.salt).hexdigest()
        if hash != self.password:
            return False

        return True

    def is_authenticated(self):
        return True


    def is_active(self):
        return True


    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id