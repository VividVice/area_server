from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
from os import getenv
from flask_sqlalchemy import SQLAlchemy

def singleton(cls):
    """A singleton decorator."""
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class Config():
    def __init__(self) -> None:
        """Initialize the Flask app and the Flask-RESTPlus API."""
        load_dotenv()
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = getenv('SERVER_SECRET_KEY')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
        CORS(self.app, supports_credentials=True)
        self.api = Api(self.app)
        self.db = SQLAlchemy(self.app)
        self.port = getenv('PORT') if getenv('PORT') else 8080

        @self.app.after_request
        def add_headers(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
            return response

    def Run(self) -> None:
        """Run the Flask app."""
        self.app.run(debug=True)

    def AddResource(self, resource, route) -> None:
        """Add a resource to the Flask-RESTPlus API.
        :param resource: The resource to add.(class Resource)
        :param route: The route to add the resource to.(str))"""
        self.api.add_resource(resource, route)

    def GetApp(self) -> Flask:
        """Get the Flask app.
        :return: The Flask app.(class Flask)"""
        return self.app

    def GetApi(self) -> Api:
        """Get the Flask-RESTPlus API.
        :return: The Flask-RESTPlus API.(class Api)"""
        return self.api

    def GetDb(self) -> SQLAlchemy:
        """Get the SQLAlchemy database.
        :return: The SQLAlchemy database.(class SQLAlchemy)"""
        return self.db