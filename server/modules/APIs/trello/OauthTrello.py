# from modules.Oauth.BaseOauthClasses import OAuth1
from os import getenv
from sys import path
path.append('../..')
from modules.utils.jsonToken import createToken
from modules.config.config import app_name


def singleton(cls):
    """A singleton decorator."""
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class  TrelloAuth():
    def __init__(self) -> None:
        self.Auth_url = "https://trello.com/1/authorize"
        self.scope = "read,write"
        self.name = app_name
        self.expiration = "never"
        self.response_type = "token"
        self.key = getenv('API_TRELLO')

    def get_authorize_url(self, username, return_url):
        state = createToken(username, False)
        url = f"{self.Auth_url}?scope={self.scope}&expiration={self.expiration}&name={self.name}"
        url += f"&response_type={self.response_type}&key={self.key}&state={state}"
        url += f"&return_url={return_url}"
        return url