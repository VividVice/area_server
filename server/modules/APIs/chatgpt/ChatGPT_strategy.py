import sys

sys.path.append('../../../')
from modules.database.DB import DataBaseOpps as DB, UserModel
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy

class ChatGPTSubStrategy(SubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        DB.SubscribeToService(user, "chatgpt", {"Areas": []})
        return {"message": "Service added."}, 200

class ChatGPTUnsubStrategy(UnSubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if user.user_services["chatgpt"] == None or user.user_services["chatgpt"] == False:
            return {"message": "Not sub to service."}, 400
        DB.UnSubcripeToService(user, "chatgpt")
        return {"message": "Service removed successfully."}, 200
