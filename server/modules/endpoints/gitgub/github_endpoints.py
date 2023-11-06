from flask import request
from flask_restful import Resource, reqparse
from sys import path
path.append('../../')
from modules.utils.jsonToken import UnpackToken
from modules.database.DB import DataBaseOpps as DB
from modules.APIs.github.OauthGithub import GithubAuth
from modules.APIs.github.github_action import get_github_email

# /github/?code={code} header: Authorization: Bearer {token}
class Github_Access(Resource):
    def post(self):
        # print("Github_Access")
        authorization_header = request.headers.get('Authorization')
        parser = reqparse.RequestParser()
        parser.add_argument('code', type=str, required=True)
        args = parser.parse_args()
        if not authorization_header:
            return {"message": "No Authorization header provided"}, 403
        payload = UnpackToken(authorization_header, True)
        if payload:
            user = DB.GetUser(payload["username"])
            if user:
                access_token = GithubAuth().get_authificated(user, args['code'])
                DB.SubcripeToService(user, "github", {"access_token": access_token, "Areas" : []})
                email = get_github_email(access_token)
                DB.AddUserOauth(user, email)
                return {"message": "Access token requst send succesfully"}, 200
            else:
                return {"message": "User not found"}, 401
        else:
            return {"message": "Invalid token"}, 403

    def options(self):
        # say everything is allowed on this route and make the browser happy and send the get request
        return {'Allow': 'PUT,GET,POST'}, 200, \
                {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': 'PUT,GET,POST, OPTIONS', \
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'}

    def head(self):
        """Checks if the user has the service
        Returns:
            200: if the user has the service
            400: if the user doesn't have the service
            403: if the request is not authenticated"""
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return {}, 403
        payload = UnpackToken(authorization_header, True)
        user = DB.GetUser(payload["username"])
        if not user or user.user_services["trello"] == False:
            return {}, 400
        return {}, 200