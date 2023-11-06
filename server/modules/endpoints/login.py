from flask import request, send_from_directory
from flask_restful import Resource, abort, reqparse
import sys
sys.path.append('../')
import modules.utils.hash as hash
# from jwt.exceptions import DecodeError
from modules.utils.jsonToken import createToken, UnpackToken, decodeToken
from modules.database.DB import DataBaseOpps as DB
from flasgger import Swagger, swag_from

class Login(Resource):
    def get(self) -> dict:
        return {'hello': 'login'}

    @swag_from('swagger_login.yml')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('password', type=str, required=False)
        parser.add_argument('rememberMe', type=bool, required=False)
        args = parser.parse_args()
        token = request.headers.get('Authorization')

        if args['username'] and args['password']:
            try:
                pass_hash = DB.GetUser(args['username']).password
                if hash.verify_password(args['password'], pass_hash):
                    token = createToken(args['username'], args['rememberMe'])
                    return {'token': token}
                else:
                    abort(401, message='Invalid credentials')
            except AttributeError:
                abort(401, message='Invalid credentials, You gave me gibberish') ## triggred when the user is not found
        elif token and token.startswith('Bearer '):
            payload = UnpackToken(token, True)
            if payload:
                User = DB.GetUser(payload["username"])
                if User:
                    User_parced_services = {}
                    for service in User.user_services: # we do this so we dont expose the password hash or access tokens
                        if User.user_services[service] != False:
                            User_parced_services[service] = True
                        else:
                            User_parced_services[service] = False
                    token = createToken(payload["username"], False)
                    return {'token': token, 'user_subs': User_parced_services}, 200 # the respone is just a token for now may change later
                else:
                    abort(401, message='Invalid User')
            else:
                abort(401, message='Expired token')
        else:
            abort(401, message='Invalid credentials')


class Register(Resource):
    def get(self) -> dict:
        return {'hello': 'register'}
    @swag_from('./swagger_login.yml')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        if args['username'] and args['password']:
            new_hash = hash.hash_password(args['password'])
            user = DB.AddUser(args['username'], new_hash)
            if user:
                token = createToken(args['username'], False)
                return {'token': token, 'user_subs': user.user_services }, 201
            else:
                abort(409, message='User already exists')
        else:
            abort(400, message='Invalid credentials')


class UserInfo(Resource):
    def get(self):
        token = request.headers.get('Authorization')
        if token and token.startswith('Bearer '):
            payload = UnpackToken(token, False)
            if payload:
                User = DB.GetUser(payload["username"])
                if User:
                    User_parced_services = {}
                    for service in User.user_services:
                        if User.user_services[service] != False:
                            User_parced_services[service] = True
                        else:
                            User_parced_services[service] = False
                    return {'user_subs': User_parced_services, 'admin': User.is_admin}, 200
                else:
                    abort(401, message='Invalid User')
            else:
                abort(401, message='Expired token')
        else:
            abort(401, message='Invalid credentials')

class RefreshToken(Resource):
    def get(self):
        token = request.headers.get('Authorization')
        if token and token.startswith('Bearer '):
            token = token[7:]
            payload = decodeToken(token)
            if payload:
                token = createToken(payload["username"], False)
                return {'token': token}, 200
            else:
                abort(401, message='Invalide token')
        else:
            abort(401, message='Invalid credentials')