from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('../')
from modules.config.config import Config
from sqlalchemy_utils import database_exists
from os import getenv

config = Config()
db:SQLAlchemy = config.GetDb()
app = config.GetApp()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'<User {self.username} With Id {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
class DataBaseOpps():
    @staticmethod
    def CreateDb() -> None:
        """Create the database only if it does not exist."""
        if not database_exists(getenv('DATABASE_URI')):
            with app.app_context():
                db.create_all()

    @staticmethod
    def GetUser(username) -> UserModel:
        """Get a user from the database. Will return None if the user does not exist."""
        return UserModel.query.filter_by(username=username).first()

    @staticmethod
    def AddUser(username, password) -> bool:
        """Add a user to the database. Will return False if the user already exists."""
        if not DataBaseOpps.GetUser(username):
            db.session.add(UserModel(username, password))
            db.session.commit()
            return True
        return False