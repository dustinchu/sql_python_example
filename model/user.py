
import sys
sys.path.append("C:/Users/dustinchu/Desktop/mysql/")
from db import db

class Note(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username, 'password': self.password}

    def create_db():
        db.create_all()
        return Note

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

