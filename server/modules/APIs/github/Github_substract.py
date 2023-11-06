import sys
sys.path.append('../../../')
from modules.database.DB import UserModel
from modules.APIs.github.OauthGithub import GithubAuth
# from OauthTrello import TrelloAuth
from modules.database.DB import DataBaseOpps as DB
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy
# from modules.APIs.trello.TrelloWebhook import Delete

class GithubSubStrat(SubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if not service_args.get('return_url'):
            raise Exception("No return url provided")
        if user.user_services["github"] != None and  user.user_services["github"] != False :
            return {"message": "Service already added."}, 400
        auth_url = GithubAuth().get_authorize_url(user.username, service_args.get('return_url'))
        return {"auth_url": auth_url}, 200

class GithubUnSubStrat(UnSubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if user.user_services["github"] == None or user.user_services["trello"] == False:
            return {"message": "Not sub to service."}, 400
        # Delete(user)
        DB.UnSubcripeToService(user, "github")
        return {"message": "Service removed successfully."}, 200
