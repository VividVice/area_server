from flask import Flask, request, jsonify
from modules.database.DB import DataBaseOpps
from modules.config.config import Config
from modules.utils.jsonToken import UnpackToken
from sys import stderr
app = Config().GetApp()

@app.route('/get_subscribed_areas', methods=['GET'])
def get_subscribed_areas():
    # Get the username from the request parameters or headers, depending on your use case
    token = request.headers.get('Authorization')
    payload = UnpackToken(token, True)
    if payload:
        user = DataBaseOpps.GetUser(payload["username"])
        if user:
            # extract from user.user_services the subscribed areas 
            # {"service_name": "trello", "Areas": [{"action": "create_card", "subbed_reactions": [{"service_name": "callr", "function_name": "make_call", "params": {"phone_number": "+972546777777"}}]}]}
            # so bacissaly extract the Areas from user.user_services["service_name"] but keep the key service_name
            # also for each reaction subbed for each action add an id that corresponds to the index of the reaction in the subbed_reactions array
            return_data = []
            for service_name in user.user_services:
                for area in user.user_services[service_name]["Areas"]:
                    area["service_name"] = service_name
                    for i in range(len(area["subbed_reactions"])):
                        area["subbed_reactions"][i]["id"] = i
                    return_data.append(area)
            return jsonify(return_data), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Username not provided"}), 403


app = Config().GetApp()