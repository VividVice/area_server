from flask import request, jsonify
from flask_restful import Resource, reqparse, abort
from sys import path
from modules.utils.jsonToken import UnpackToken
from modules.database.DB import DataBaseOpps as DB
from modules.APIs.AREA_lists import action_list, reaction_list, Create_Area
from modules.utils.error_classes import UnknowService, FailedExecution
import traceback
import sys
path.append('../../')


""" Example of a valid request
Header: { "Authorization" : "Bearer  <token>" }
{
    "action_service": "trello",
    "action_name": "createBoard",
    "action_params" : {},
    "reaction_service": "trello",
    "reaction_name": "createCard",
    "reaction_params": {
        "list_id": "5f9b7b4b7b7b7b7b7b7b7b7b",
        "card_name": "test card"
    }
"""
class Area_Sub(Resource):
    def post(self):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return {"message": "No Authorization header provided"}, 403
        payload = UnpackToken(authorization_header, True)
        if not payload:
            return {"message": "Invalid credentials"}, 403
        user = DB.GetUser(payload["username"])
        parser = reqparse.RequestParser()
        parser.add_argument('action_service', type=str, required=True)
        parser.add_argument('action_name', type=str, required=True)
        parser.add_argument('action_params', type=dict, required=True)
        parser.add_argument('reaction_service', type=str, required=True)
        parser.add_argument('reaction_name', type=str, required=True)
        parser.add_argument('reaction_params', type=dict, required=True)
        args = parser.parse_args()
        try :
            ParserAction(user, args['action_service'], args['action_name'], args['action_params'])
            ParserReaction(user, args['reaction_service'], args['reaction_name'], args['reaction_params'])
            Create_Area(user=user, action_service=args['action_service'], action_name=args['action_name'], action_params=args['action_params'],
                        reaction_service=args['reaction_service'], reaction_name=args['reaction_name'], reaction_params=args['reaction_params'])
            print("user.user_services:", user.user_services)
        except Exception as e:
            print(e, file=sys.stderr, end="")
            traceback.print_exc()
            return {"message": str(e)}, 400
        return {"message": "AREA added successfully."}, 200

def ParserAction(user, service_name, action_name, action_params):
    if service_name not in action_list:
        raise UnknowService(service_name)
    if action_name not in list(map(lambda x: x["name"], action_list[service_name])):
        raise UnknowService(action_name)

def ParserReaction(user, service_name, reaction_name, reaction_params):
    if service_name not in reaction_list:
        raise UnknowService(service_name)
    if reaction_name not in list(map(lambda x: x["name"], reaction_list[service_name])):
        raise UnknowService(reaction_name)
"""
the idea is parse the action and reaction and check if they are valid
and then maybe call the service's action setup method and pass the reaction's params to it
"""