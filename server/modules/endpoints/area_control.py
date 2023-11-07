from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from modules.database.DB import DataBaseOpps as DB
from modules.config.config import Config
from modules.utils.jsonToken import UnpackToken
from sys import stderr
app = Config().GetApp()

class Area_Control(Resource):
    def get():
        # Get the username from the request parameters or headers, depending on your use case
        token = request.headers.get('Authorization')
        payload = UnpackToken(token, True)
        if payload:
            user = DB.GetUser(payload["username"])
            if user:
                # extract from user.user_services the subscribed areas 
                # {"service_name": "trello", "Areas": [{"action": "create_card", "subbed_reactions": [{"service_name": "callr", "function_name": "make_call", "params": {"phone_number": "+972546777777"}}]}]}
                # so bacissaly extract the Areas from user.user_services["service_name"] but keep the key service_name
                # also for each reaction subbed for each action add an id that corresponds to the index of the reaction in the subbed_reactions array
                return_data = []
                for service_name in user.user_services:
                    if user.user_services[service_name] == False:
                        continue
                    for area in user.user_services[service_name]["Areas"]:
                        for reaction in area["subbed_reactions"]:
                            return_data.append({
                                "action_service_name": service_name,
                                "action": area["action"],
                                "reaction_name": reaction["reaction_name"],
                                "reaction_service_name": reaction["service_name"],
                                "id": reaction["id"],
                                "params_reaction": reaction["params"]
                            })
                return jsonify(return_data), 200
            else:
                return jsonify({"error": "User not found"}), 404
        else:
            return jsonify({"error": "Username not provided"}), 403

    def post(self):
        token = request.headers.get('Authorization')
        payload = UnpackToken(token, True)
        parser = reqparse.RequestParser()
        parser.add_argument('action_service_name', type=str, required=True)
        parser.add_argument('action', type=str, required=True)
        parser.add_argument('id', type=int, required=True)
        args = parser.parse_args()
        if payload:
            user = DB.GetUser(payload["username"])
            if user :
                try :
                    for area in user.user_services[args["action_service_name"]]["Areas"]:
                        if area["action"] == args["action"]:
                            area["subbed_reactions"].pop(args["id"])
                            # check if is it is the last reaction if so execute delete webhook
                            if len(area["subbed_reactions"]) == 0:
                                # delete webhook
                                # delete the action as well
                                user.user_services[args["action_service_name"]]["Areas"].remove(area)
                            DB.Commit()
                            print("user_services", user.user_services, file=stderr)
                            return {"message": "Area deleted"}, 200
                    return {"message": "Area not found"}, 401
                except KeyError:
                    return {"message": "Service not subbed"}, 401
            else :
                return {"message": "User not found"}, 404
        else:
            return {"message": "JWS is invalid"}, 403