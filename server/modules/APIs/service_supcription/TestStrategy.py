import sys
from flask_sqlalchemy import SQLAlchemy
sys.path.append('../../../')
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy
from modules.database.DB import UserModel, DataBaseOpps as DB
from modules.config.config import Config

db:SQLAlchemy = Config().GetDb()

## this is a test strategy for the test service. implement one for each service
class TestSubcrpibeStrategy(SubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        DB.SubcripeToService(user, "testSub", service_args['enabled'])
        print ("Subscribed to testSub")
        # should return a valide responce object compatible with flask_restful
        return {"message": "Service added successfully."}, 200
class TestUnSubcrpibeStrategy(UnSubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        DB.UnSubcripeToService(user, "testSub")
        print ("Unsubscribed from testSub")
        return {"message": "Service removed successfully."}, 200