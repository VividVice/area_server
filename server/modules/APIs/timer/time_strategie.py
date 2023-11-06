import sys

sys.path.append('../../../')
from modules.database.DB import UserModel
from modules.database.DB import DataBaseOpps as DB
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy

class TimerSubstrtegy(SubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        DB.SubscribeToService(user, "time", {"Areas": []})
        return {"message": "Service added successfully."}, 200

class TimerUnsubStrategy(UnSubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if user.user_services["callr"] == None or user.user_services["callr"] == False:
            return {"message": "Not sub to service."}, 400
        DB.UnSubcripeToService(user, "time")
        return {"message": "Service removed successfully."}, 200
