import sys
import callr

sys.path.append('../../../')
from modules.database.DB import DataBaseOpps as DB, UserModel
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy

class CallrSubStrategy(SubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if not service_args.get('username'):
            raise Exception("No username provided")
        if not service_args.get('password'):
            raise Exception("No password provided")
        # check if the user is already subscribed to the service
        if user.user_services["callr"] != None and  user.user_services["callr"] != False :
            print(user.user_services["callr"])
            return {"message": "Service already added."}, 201
        auth_url = "http://localhost:8081/create-area"
        try:
            api = callr.Api(service_args.get('username'), service_args.get('password'))

            result = api.call('did/store.get_quota_status')
            DB.SubcripeToService(user, "callr", {"username": service_args.get('username'),
                                                 "password": service_args.get('password'),
                                                 "Areas" : []})
            print(result)
            return {"auth_url": auth_url}, 200
        except Exception as e:
            return {"error": str(e)}, 400

class CallrUnsubStrategy(UnSubscriptionStrategy):
    def execute(self, user:UserModel, service_args: dict):
        if user.user_services["callr"] == None or user.user_services["callr"] == False:
            return {"message": "Not sub to service."}, 400
        DB.UnSubcripeToService(user, "callr")
        return {"message": "Service removed successfully."}, 200
