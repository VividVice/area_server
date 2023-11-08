from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import time
from sys import path
path.append('../')
from modules.APIs.trello.Trello_actions import get_service_info as trello_info
from modules.APIs.weather.weather_Action import get_service_info as weather_info
from modules.APIs.nasa.nasa_action import get_service_info as nasa_info
from modules.APIs.timer.time_action import get_service_info as timer_info
from modules.APIs.callr.Callr_actions import get_serice_info as callr_info
from modules.APIs.chatgpt.ChatGPT_actions import get_service_info as chat_info
# example of service methods for info they should follow sigleton pattern

def get_server_status():
    # serveces list
    services = [ trello_info, weather_info, nasa_info, timer_info, callr_info, chat_info]
    # Create the server_info dictionary
    server_info = {
        "client": {"host": request.remote_addr},
        "server": {
            "current_time": int(time.time()),
            "services": [],
        },
    }

    # Add the service to the services list
    for service in services:
        try:
            server_info["server"]["services"].append(service())
        except AttributeError :
            pass

    # Return the server_info dictionary as json
    return jsonify(server_info)

class AboutResource(Resource):
    def get(self):
        return get_server_status()