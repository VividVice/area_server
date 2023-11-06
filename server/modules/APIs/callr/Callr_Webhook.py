from os import getenv
from sys import path, stderr
import traceback
path.append('../')
from flask import request
from flask_restful import Resource
from modules.database.DB import DataBaseOpps as DB, UserModel
from modules.APIs.callr.Callr_actions import create_webhook
from modules.utils.FuncIvoker import FuncInvoker
from modules.utils.getServerIp import get_server_ip
from modules.utils.error_classes import FailedExecution

def get_endpoint() -> str:
    return 'callr/webhook'

# setup all webhooks for a specific user (not used)
def SetupAll(User:UserModel) -> None:
    webhook_data = {
        'description': f'webhook for callr user',
        'callbackURL': f'{getenv("SERVER_URL")}/{get_endpoint()}/?user_name={User.username}',
        'idModel': 1,
        'active': True,
        'type': ['callOutboundHangup', 'callInboundStart', 'callOutboundStart', 'mediaRecording', 'callInboundHangup', 'billingCredit', 'sendSms', 'didAssigned', 'didUnassigned']
    }
    print(webhook_data)

# setup a webhook for a specific user
def Setup(User:UserModel, type:str, params = None) -> None:
    print("the setup function gets called", file=stderr)
    create_webhook(User, type, f'http://{get_server_ip()}/{get_endpoint()}/?user_name={User.username}', params)

def Delete(User:UserModel) -> None:
    pass
    # user_id =  get_user_id(User)
    # webhooks = get_webhooks_for_user(User)
    # for webhook in webhooks:
    #     delete_webhook(User, webhook['id'])

# handle the webhook for callr
# callr crush
class WebHookCallr(Resource):
    def post(self):
        """Handle the webhook for Callr."""
        print("request.args:", request.args)
        user_name = request.args.get('user_name')
        user = DB.GetUser(user_name)
        if user:
            try:
                # loop though the Areas in user.service_args["callr"]["Areas"] and check if the action_type is the same as an entry in the Areas with prop action
                # if it is then call the functions inside it via FuncInvoker
                action_type = request.json['action']['type']
                for area in user.user_services["callr"]["Areas"]:
                    if area["action"] == action_type:
                        for reaction in area["subbed_reactions"]:
                            # call the function adding the user as the first argument and then unpack the params keys as argument names and the values as the values the params is a dict
                            FuncInvoker(reaction["service_name"],reaction["function_name"], user=user, **reaction["params"])
                return {'message': 'success'}, 200
            except Exception as e:
                traceback.print_exc()
                print(e)
                return {'message': e}, 400
        else:
            return {'message': 'user not found'}, 400

    def head(self):
        """Handle the webhook for callr."""
        return {'message': 'success'}, 200


# user is subcriped to a webhook boardCreated and executes callr CreateCard when the webhook is called, the args are bassed beforehand to the /create_AREA endpoint