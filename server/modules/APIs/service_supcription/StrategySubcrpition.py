import sys
sys.path.append('../../..')
from modules.database.DB import UserModel

class SubscriptionStrategy:
    def execute(self, user:UserModel, service_args:dict):
        raise NotImplementedError("Subclasses must implement execute")


class UnSubscriptionStrategy:
    def execute(self, user:UserModel, service_args:dict):
        raise NotImplementedError("Subclasses must implement execute")
