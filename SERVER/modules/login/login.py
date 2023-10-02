from flask import request
from flask_restful import Resource, abort, reqparse
import sys
sys.path.append('../')
import modules.utils.hash as hash
# from jwt.exceptions import DecodeError
from modules.utils.jsonToken import createToken, decodeToken
from modules.database.DB import DataBaseOpps as DB
import datetime

class Login(Resource):
    # should remove, this is just for testing
    def get(self) -> dict:
        return {'hello': 'login'}

    def post(self):

        """Corresponds to the /login route. Handles login and token creation.
        Can send a username and password or a token.
        If a token is sent it will be validated and a new token will be sent back if valide.
        If a username and password is sent it will be validated and a token will be sent back if valide.
        Error codes: 401 - Invalid credentials or token Expired aka request new Login, 200 - Request if valided"""

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
                abort(401, message='Invalid credentials')
        elif token and token.startswith('Bearer '):
            try:
                payload = decodeToken(token[7:])
                print(payload)
                print("there is something wrong" if DB.GetUser(payload["username"]) == None else "all good")
                # return {'token': token, 'payload': payload, 'servertime': int(datetime.datetime.utcnow().timestamp())}, 200 # the respone is just a token for now may change later
                if payload["exp"] > int(datetime.datetime.utcnow().timestamp()):
                    if DB.GetUser(payload["username"]):
                        token = createToken(payload["username"], False)
                        return {'token': token}, 200 # the respone is just a token for now may change later
                    else:
                        abort(401, message='Invalid token')
                else:
                    abort(401, message='Expired token')
            except Exception as e:
                abort(401, message='Invalid token, Exception: ' + str(e))
        else:
            abort(401, message='Invalid credentials')

    @staticmethod
    def IsAuthed(token):
        try:
            payload = decodeToken(token)
            try:
                return payload["exp"] < int(datetime.datetime.utcnow().timestamp())
            except AttributeError:
                return False
        except Exception as e:
            return False


class Register(Resource):
    # should remove, this is just for testing
    def get(self) -> dict:
        return {'hello': 'register'}

    def post(self):
        """Corresponds to the /register route. Handles registration and token creation.
        Can send a username and password.
        If a username and password is sent it will be validated and new user will be added to BD
        A token will be sent back as well.
        Error codes: 409 - User already exists, 400 - Invalid credentials, 201 - Request if valided"""
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        if args['username'] and args['password']:
            new_hash = hash.hash_password(args['password'])
            if DB.AddUser(args['username'], new_hash):
                token = createToken(args['username'], False)
                return {'token': token}, 201 # the respone is just a token for now may change later
            else:
                abort(409, message='User already exists')
        else:
            abort(400, message='Invalid credentials')

