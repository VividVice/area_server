from abc import ABC, abstractmethod
import requests

class OAuthBase(ABC):
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None

    @abstractmethod
    def get_authorization_url(self):
        pass

    @abstractmethod
    def fetch_access_token(self, code):
        pass

    @abstractmethod
    def make_authenticated_request(self, url, method='GET', data=None, headers=None):
        pass

class OAuth1(OAuthBase):
    def __init__(self, client_id, client_secret, redirect_uri, request_token_url, access_token_url):
        super().__init__(client_id, client_secret, redirect_uri)
        self.request_token_url = request_token_url
        self.access_token_url = access_token_url
        self.oauth_token = None
        self.oauth_token_secret = None

    def get_authorization_url(self):
        # Implement OAuth 1 authorization URL generation
        # You can use self.client_id, self.client_secret, and self.request_token_url
        pass

    def fetch_access_token(self, oauth_verifier):
        # Implement OAuth 1 access token retrieval
        # You can use self.client_id, self.client_secret, self.oauth_token, self.oauth_token_secret
        pass

    def make_authenticated_request(self, url, method='GET', data=None, headers=None):
        # Implement OAuth 1 authenticated request
        # You can use self.client_id, self.client_secret, self.access_token, and self.oauth_token_secret
        pass

class OAuth2(OAuthBase):
    def __init__(self, client_id, client_secret, redirect_uri, authorization_url, token_url):
        super().__init__(client_id, client_secret, redirect_uri)
        self.authorization_url = authorization_url
        self.token_url = token_url

    def get_authorization_url(self):
        # Implement OAuth 2 authorization URL generation
        # You can use self.client_id, self.redirect_uri, and self.authorization_url
        pass

    def fetch_access_token(self, code):
        # Implement OAuth 2 access token retrieval
        # You can use self.client_id, self.client_secret, self.redirect_uri, self.token_url
        pass

    def make_authenticated_request(self, url, method='GET', data=None, headers=None):
        # Implement OAuth 2 authenticated request
        # You can use self.access_token
        pass
