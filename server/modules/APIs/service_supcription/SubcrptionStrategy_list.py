import sys
sys.path.append('../../..')
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy
from modules.APIs.APIs_list import list_api
from modules.utils.error_classes import UnknowService

"""
    Ways to set up a service:
    Trello
        {
            "service": "trello",
            "service_args": {
                "return_url": the url where you want to load in the front end after auth,
                }
        }
        After make a get request to /trello/?access_token={the_access_token given by trello}
        make sure you always send the header Authorization: Bearer {JWT token} with EVERY request
"""
class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

class SubscriptionStrategyFactory(Singleton):
    def __init__(self):
        self.Strategy_dict = {}
        for key, value in list_api.items():
            self.Strategy_dict[key] = value["subscribe"]
    def GetStrategy(self, service_name: str) -> SubscriptionStrategy:
        strategy = self.Strategy_dict.get(service_name)
        if not strategy:
            raise UnknowService(service_name)
        return strategy

class UnSubscriptionStrategyFactory(Singleton):
    def __init__(self):
        self.Strategy_dict = {}
        for key, value in list_api.items():
            self.Strategy_dict[key] = value["unsubscribe"]
    def GetStrategy(self, service_name: str) -> UnSubscriptionStrategy:
        strategy = self.Strategy_dict.get(service_name)
        if not strategy:
            raise UnknowService(service_name)
        return strategy