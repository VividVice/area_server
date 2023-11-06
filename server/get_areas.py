from flask import Flask, request, jsonify
from modules.database.DB import DataBaseOpps
from modules.config.config import Config
from modules.utils.jsonToken import UnpackToken

app = Config().GetApp()

@app.route('/get_subscribed_areas', methods=['GET'])
def get_subscribed_areas():
    # Get the username from the request parameters or headers, depending on your use case
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        payload = UnpackToken(token, False)
    if payload:
        user = DataBaseOpps.GetUser(payload["username"])
        if user:
            subscribed_areas = [service for service, value in user.user_services.items() if value]
            return jsonify(subscribed_areas)
        else:
            return jsonify({"error": "User not found"})
    else:
        return jsonify({"error": "Username not provided"})


app = Config().GetApp()