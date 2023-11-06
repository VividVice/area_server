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
    print(token, file=stderr)
    payload = UnpackToken(token, True)
    if payload:
        user = DataBaseOpps.GetUser(payload["username"])
        if user:
            subscribed_areas = [service for service, value in user.user_services.items() if value]
            print(subscribed_areas, file=stderr)
            return jsonify(subscribed_areas), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Username not provided"}), 403


app = Config().GetApp()