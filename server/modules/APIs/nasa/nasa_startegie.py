import sys

sys.path.append('../../../')
from modules.database.DB import UserModel
from modules.database.DB import DataBaseOpps as DB
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy

class NasaSubstrtegy(SubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        DB.SubscribeToService(user, "nasa", {"Areas": []})
        return {"message": "Service added successfully."}, 200

class NasaUnsubStrategy(UnSubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        DB.UnSubcripeToService(user, "nasa")
        return {"message": "Service removed successfully."}, 200
