from os import getenv
from sys import path, stderr
import traceback
path.append('../')
from flask import request
from flask_restful import Resource
from modules.database.DB import DataBaseOpps as DB, UserModel
from modules.APIs.trello.Trello_actions import get_user_id, post_webhook, delete_webhook, get_webhooks_for_user
from modules.config.config import Config
from modules.utils.FuncIvoker import FuncInvoker
from modules.utils.getServerIp import get_server_ip
from modules.utils.error_classes import FailedExecution
app = Config().GetApp()

def get_endpoint() -> str:
    return 'trello/webhook'

# setup all webhooks for a specific user (not used)
def SetupAll(User:UserModel) -> None:
    user_id =  get_user_id(User)
    webhook_data = {
        'description': f'webhook for user {user_id}',
        'callbackURL': f'{getenv("SERVER_URL")}/{get_endpoint()}/?user_name={User.username}',
        'idModel': user_id,
        'active': True,
        # it should be do creating/updating/deleting a board, list, card, member, etc...
        'type': ['createCard', 'updateCard', 'deleteCard', 'createList', 'updateList', 'deleteList', 'createBoard', 'updateBoard', 'deleteBoard', 'createMember', 'updateMember', 'deleteMember']
    }
    print(webhook_data)
    post_webhook(User, webhook_data)

# setup a webhook for a specific user
def Setup(User:UserModel, type:str, params = None) -> None:
    user_id =  get_user_id(User)
    webhook_data = {
        'description': f'webhook for user {user_id}',
        'callbackURL': f'{get_server_ip()}/{get_endpoint()}/?user_name={User.username}',
        'idModel': user_id,
        'active': True,
        'type': [type]
    }
    print("webhook_data:", webhook_data)

    post_webhook(User, webhook_data)

def DeleteAll(User:UserModel) -> None:
    user_id =  get_user_id(User)
    webhooks = get_webhooks_for_user(User)
    for webhook in webhooks:
        delete_webhook(User, webhook['id'])

def Delete(User:UserModel, action_name) -> None:
    user_id =  get_user_id(User)
    webhooks = get_webhooks_for_user(User)
    if webhooks == None:
        return
    for webhook in webhooks:
        if webhook['description'] == f'webhook for user {user_id}':
            # if webhook['type'] == action_name:
            print("deleting webhook:", webhook, file=stderr)
            #     delete_webhook(User, webhook['id'])

# handle the webhook for trello
# trello crush
class WebHookTrello(Resource):
    def post(self):
        """Handle the webhook for trello."""
        print("request.args:", request.args)
        user_name = request.args.get('user_name')
        user = DB.GetUser(user_name)
        if user:
            try:
                # loop though the Areas in user.service_args["trello"]["Areas"] and check if the action_type is the same as an entry in the Areas with prop action
                # if it is then call the functions inside it via FuncInvoker
                action_type = request.json['action']['type']
                for area in user.user_services["trello"]["Areas"]:
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
        """Handle the webhook for trello."""
        return {'message': 'success'}, 200


# user is subcriped to a webhook boardCreated and executes trello CreateCard when the webhook is called, the args are bassed beforehand to the /create_AREA endpoint