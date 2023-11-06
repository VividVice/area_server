from flask import request
from flask_restful import Resource, abort, reqparse
import sys
sys.path.append('../')
# from jwt.exceptions import DecodeError
from modules.utils.jsonToken import createToken
from modules.APIs.github.OauthGithub import GithubAuth
from modules.APIs.github.github_action import get_github_email
from modules.database.DB import DataBaseOpps as DB
from modules.utils.hash import generate_username

class GitHubOauthAuthorization(Resource):
    """This class is used to get the authorization url for github"""
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('return_url', type=str, required=True)
        args = parser.parse_args()
        auth_url = GithubAuth().get_authorize_url("unknown",args['return_url'])
        return {'auth_url': auth_url}, 200

class GitHubOauthAccess(Resource):
    def get(self):
        code = request.args.get('code')
        if not code:
            abort(400, message='No code provided')
        access_token = GithubAuth().unknown_user_auth(code)
        if not access_token:
            abort(400, message='error getting access token')
        email = get_github_email(access_token)
        # check if the user is already registered
        user = DB.GetUserByOauthEmail(email)
        if not user:
            # register the user
            username = generate_username(set(DB.GetAllUsernames()))
            user = DB.AddUser(username)
            # subcribe the user to the service github
            DB.SubcripeToService(user, "github", {"access_token": access_token, "Areas" : []})
            DB.AddUserOauth(user, email)
            token = createToken(user.username, False)
            User_parced_services = {}
            for service in user.user_services: # we do this so we dont expose the password hash or access tokens
                if user.user_services[service] != False:
                    User_parced_services[service] = True
                else:
                    User_parced_services[service] = False
            return {'token': token, 'user_subs': User_parced_services}, 200
        else: # the user exists log them in
            token = createToken(user.username, False)
            User_parced_services = {}
            for service in user.user_services:
                if user.user_services[service] != False:
                    User_parced_services[service] = True
                else:
                    User_parced_services[service] = False
            return {'token': token, 'user_subs': User_parced_services}, 200