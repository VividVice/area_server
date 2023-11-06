from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy_json import MutableDict
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
    # add the api services that the user has subscribed to
    user_services = db.Column(MutableDict.as_mutable(db.JSON), nullable=False, default={})
    github_account_email = db.Column(db.String(30), nullable=True, default=None) # used for OAuth
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'<User {self.username} With Id {self.id} : {self.services}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'services': self.user_services,
            'is_admin': self.is_admin
        }

class ServiceModel(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(30), nullable=False)
    users = db.relationship('UserModel', secondary='user_services', backref=db.backref('services', lazy='dynamic'))

    users_service = db.Table('user_services', db.Model.metadata,
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('service_id', db.Integer, db.ForeignKey('services.id'))
    )

def CreateDb() -> None:
    from modules.APIs.APIs_list import list_api # do not move this import to the top of the file or dire things will happen
    """Create the database only if it does not exist."""
    if not database_exists(getenv('DATABASE_URI')):
        with app.app_context():
            db.create_all()
            for service_name in list_api.keys():
                service = ServiceModel(names=service_name)
                db.session.add(service)
            # create the admin user
            admin = UserModel(username=getenv('ADMIN_USERNAME'), password=getenv('ADMIN_PASSWORD'))
            admin.is_admin = True
            db.session.add(admin)
            db.session.commit()