import sys

sys.path.append('../../../')
from modules.database.DB import UserModel
from modules.APIs.trello.OauthTrello import TrelloAuth
# from OauthTrello import TrelloAuth
from modules.database.DB import DataBaseOpps as DB
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy
# from modules.APIs.trello.TrelloWebhook import Delete

class TrelloSubStrat(SubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if not service_args.get('return_url'):
            raise Exception("No return url provided")
        # check if the user is already subscribed to the service
        if user.user_services["trello"] != None and  user.user_services["trello"] != False :
            print(user.user_services["trello"])
            return {"message": "Service already added."}, 201
        auth_url = TrelloAuth().get_authorize_url(user.username, service_args['return_url'])
        return {"auth_url": auth_url}, 200

class TrelloUnSubStrat(UnSubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if user.user_services["trello"] == None or user.user_services["trello"] == False:
            return {"message": "Not sub to service."}, 400
        # Delete(user)
        DB.UnSubcripeToService(user, "trello")
        return {"message": "Service removed successfully."}, 200
