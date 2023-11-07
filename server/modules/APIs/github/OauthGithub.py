# Import necessary libraries
import requests
from flask import Flask, request, redirect, session, url_for
from os import getenv
from modules.utils.jsonToken import createToken
from modules.database.DBsetup import UserModel
from modules.utils.error_classes import AuthCompromisedError

def singleton(cls):
    """A singleton decorator."""
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class GithubAuth():
    def __init__(self) -> None:
        self.Auth_url = "https://github.com/login/oauth/authorize"
        self.Access_token_url = "https://github.com/login/oauth/access_token"
        # the scope has to have access to the username and be able to create, read, update, and delete repos
        self.scope = "user+repo"
        self.client_id = getenv('GITHUB_CLIENT_ID')
        self.client_secret = getenv('GITHUB_CLIENT_SECRET')

    def get_authorize_url(self, username, return_url):
        state = "Yestest"
        url = f"{self.Auth_url}?scope={self.scope}&client_id={self.client_id}&state={state}"
        url += f"&return_url={return_url}"
        return url

    # the callback url is /github-callback?username={username}
    def get_authificated(self, user:UserModel, code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
        }
        headers = {'Accept': 'application/json'}
        responce = requests.post(self.Access_token_url, data=data, headers=headers)
        # is thers is responce json then retrun the access token if not then return None
        try :
            return responce.json()['access_token']
        except:
            return None

    def unknown_user_auth(self, code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
        }
        headers = {'Accept': 'application/json'}
        responce = requests.post(self.Access_token_url, data=data, headers=headers)
        # is thers is responce json then retrun the access token if not then return None
        try :
            return responce.json()['access_token']
        except:
            return None



# CLIENT_ID = getenv('GITHUB_ID')
# CLIENT_SECRET = getenv('GITHUB_SECRET')
# # Create a Flask application
# app = Flask(__name__)
# app.secret_key = getenv('API_SECRET')
# # GitHub OAuth URLs
# GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize'
# GITHUB_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

# # Redirect users to GitHub for authentication
# @app.route('/login')
# def login():
#     return redirect(f"{GITHUB_AUTH_URL}?client_id={CLIENT_ID}")

# # Handle the GitHub callback and exchange the code for an access token
# @app.route('/github-callback')
# def github_callback():
#     code = request.args.get('code')

#     # Request an access token using the code
#     response = requests.post(
#         'https://github.com/login/oauth/access_token',
#         data={
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#             'code': code
#         },
#         headers={'Accept': 'application/json'}
#     )

#     if response.status_code == 200:
#         data = response.json()
#         access_token = data.get('access_token')

#         # Now you have the access token, you can use it for making API requests
#         # Store the access token or use it as needed in your application

#         return f'GitHub OAuth successful! Access token obtained: {access_token}'
#     else:
#         return 'GitHub OAuth failed.'


# # Access a protected resource using the obtained access token
# @app.route('/protected')
# def protected_resource():
#     access_token = session.get('access_token')
#     if access_token:
#         headers = {'Authorization': f'Bearer {access_token}'}
#         response = requests.get('https://api.github.com/user', headers=headers)
#         user_data = response.json()
#         return f'Hello, {user_data["login"]}! Your GitHub ID is {user_data["id"]}'
#     else:
#         return 'Access token not found. Please authenticate with GitHub first.'

# if __name__ == '__main__':
#     app.run(debug=True)