from flask import request, jsonify
from flask_restful import Resource
from sys import path
path.append('../../')
from modules.config.config import Config
from modules.utils.jsonToken import UnpackToken
from modules.database.DB import DataBaseOpps as DB
from modules.APIs.trello.TrelloWebhook import Setup, TrelloHandleHook
app = Config().GetApp()

class Trello_Access(Resource):
    def get(self):
        print("Trello_Access")
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return {"message": "No Authorization header provided"}, 403
        payload = UnpackToken(authorization_header, True)
        if payload:
            access_token = request.args.get('access_token')
            if not access_token:
                return {"message": "No access token provided"}, 403
            user = DB.GetUser(payload["username"])
            if user:
                print("user found")
                if DB.SubcripeToService(user, "trello", {"access_token": access_token}) == False:
                    print("why is this false")
                    return {"message": "DB error"}, 502
                else:
                    print("service added")
                    print(user.user_services)
                Setup(user)
                return {"message": "Service added successfully."}, 200
            else:
                return {"message": "User not found"}, 401

        else:
            return {"message": "Invalid credentials"}, 403

    def options(self):
        # say everything is allowed on this route and make the browser happy and send the get request
        return {'Allow': 'PUT,GET,POST'}, 200, \
                {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': 'PUT,GET,POST, OPTIONS', \
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'}


@app.route('/trello/list')
def Trello_get_lists():
    authorization_header = request.headers.get('Authorization')
    if not authorization_header:
        return {"message": "No Authorization header provided"}, 403
    payload = UnpackToken(authorization_header, True)
    if payload:
        user = DB.GetUser(payload["username"])
        if user:
            return jsonify(user.user_services["trello"]["list_created"]), 200
        else:
            return jsonify({"message": "User not found"}), 401

    else:
        return jsonify({"message": "Invalid credentials"}), 403