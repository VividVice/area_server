from flask import Flask, request, jsonify
from modules.database.DB import DataBaseOpps
from modules.config.config import Config

app = Config().GetApp()

@app.route('/get_subscribed_areas', methods=['GET'])
def get_subscribed_areas():
    # Get the username from the request parameters or headers, depending on your use case
    username = request.args.get('username')

    if username:
        user = DataBaseOpps.GetUser(username)
        if user:
            subscribed_areas = [service for service, value in user.user_services.items() if value]
            return jsonify(subscribed_areas)
        else:
            return jsonify({"error": "User not found"})
    else:
        return jsonify({"error": "Username not provided"})


app = Config().GetApp()