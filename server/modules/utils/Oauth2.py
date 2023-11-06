import requests

class OAuth2Session:
    def __init__(self, client_id, client_secret, authorization_url, token_url, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorization_url = authorization_url
        self.token_url = token_url
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.token = None

    def get_authorization_url(self):
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'response_type': 'code',
        }
        return f"{self.authorization_url}?{self._encode_params(params)}"

    def fetch_token(self, code):
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        response = requests.post(self.token_url, data=data)
        if response.status_code == 200:
            self.token = response.json()
            return self.token
        return None

    def SetToken(self, token):
        self.token = token

    def request(self, method, url, data=None, headers=None):
        if self.token is None:
            raise Exception("Token not available. Please fetch/set a token first.")

        if headers is None:
            headers = {}
        headers['Authorization'] = f"Bearer {self.token['access_token']}"

        response = requests.request(method, url, data=data, headers=headers)
        return response

    def _encode_params(self, params):
        return '&'.join([f"{key}={value}" for key, value in params.items()])