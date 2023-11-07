from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('../')
from modules.config.config import Config
from modules.utils.error_classes import UnknowService, UnknowUser
from modules.database.DBsetup import UserModel, ServiceModel

config = Config()
db:SQLAlchemy = config.GetDb()
app = config.GetApp()


class DataBaseOpps():
    @staticmethod
    def GetUser(username) -> UserModel :
        """Get a user from the database. Will return None if the user does not exist."""
        return UserModel.query.filter_by(username=username).first()

    @staticmethod
    def AddUser(username, password=None) -> UserModel :
        from modules.APIs.APIs_list import list_api # do not move this import to the top of the file or dire things will happen
        """Add a user to the database. Sets the currently supported services to False(not enabled).
        Will return False if the user already exists.
        Will return the user if it was added successfully."""
        if not DataBaseOpps.GetUser(username):
            JsonServices = {}
            for service_name in list_api.keys():
                JsonServices[service_name] = False # put whatever afterwards aka any type of data
            if password:
                user = UserModel(username=username, password=password)
            else:
                user = UserModel(username=username, password="")
            user.user_services = JsonServices
            db.session.add(user)
            db.session.commit()
            return user
        return False
    @staticmethod
    def DeleteUser(user:UserModel) -> bool:
        """Delete a user from the database. Will return False if the user does not exist.
        Will return True if the user was deleted successfully.
        in the future it should do unsubscription from all services first"""
        if user:
            # UnsubFromAllServices(user)
            db.session.delete(user)
            db.session.commit()
            return True
        return False


    @staticmethod
    def GetUserByOauthEmail(email:str) -> UserModel:
        """Get a user from the database by the email used for the OAuth. Will return None if the user does not exist."""
        return UserModel.query.filter_by(github_account_email=email).first()

    @staticmethod
    def GetAllUsernames() -> list:
        """Get all the usernames from the database. Will return an empty list if there are no users."""
        return [user.username for user in UserModel.query.all()]

    @staticmethod
    def AddUserOauth(user:UserModel, email:str) -> bool:
        """Update the user's OAuth email. Will return False if the user does not exist."""
        if user:
            user.github_account_email = email
            db.session.commit()
            return True
        return False

    @staticmethod
    def SubcripeToService(user:UserModel, service:str, value:any) -> bool:
        """Add a service subscription to the user. Will return False if the user already has the service.
        If the user does not exist, it will raise an UnknowUser exception."""
        if user:
            service_obj = ServiceModel.query.filter_by(names=service).first()
            if not service_obj:
                raise UnknowService(service)
            # user.services is a json object that contains all the services that the user has subscribed to check if the service is not false it means that the user has subscribed to it
            if service in user.user_services and user.user_services[service] != False:
                return False
            print("the value is", value)
            services = user.user_services
            services[service] = value # can be anything
            user.user_services = services
            # add the user to the service
            service_obj.users.append(user)
            db.session.commit()
            return True
        raise UnknowUser(user)

    @staticmethod
    def IsAdmin(user:UserModel) -> bool: # may be useless but we will see
        """Check if the user is an admin. Will return False if the user is not an admin.
        If the user does not exist, it will raise an UnknowUser exception."""
        if user:
            return user.is_admin
        raise UnknowUser(user)

    @staticmethod
    def UnSubcripeToService(user:UserModel, service:str) -> bool:
        """Remove a service subscription from the user. Will return False if the user does not have the service.
        If the user does not exist, it will raise an UnknowUser exception."""
        if user:
            service_obj = ServiceModel.query.filter_by(names=service).first()
            if not service_obj:
                raise UnknowService(service)
            # user.user_services is a json object that contains all the services that the user has subscribed to check if the service is not false it means that the user has subscribed to it
            if service not in user.user_services or user.user_services[service] == False:
                return False
            services = user.user_services
            services[service] = False
            user.user_services = services
            # remove the user from the service
            service_obj.users.remove(user)
            db.session.commit()
        raise UnknowUser(user)

    @staticmethod
    def getSubServiceUsers(service_name) -> list:
        service_obj = ServiceModel.query.filter_by(names=service_name).first()
        if not service_obj:
            raise UnknowService(service_name)
        return service_obj.users

    @staticmethod
    def addToServiceArgs(User, service_name, value_name, value) -> None:
        if User:
            services = User.user_services
            old_value:dict = services[service_name]
            old_value[value_name] = value
            User.user_services = services
            db.session.commit()
        raise UnknowUser(User)


    @staticmethod
    def getServiceArgs(User:UserModel, service_name:str) -> dict:
        if User:
            services = User.user_services
            return services[service_name]
        raise UnknowUser(User)

    @staticmethod
    def Commit() -> None:
        """Commit the changes to the database."""
        db.session.commit()

    @staticmethod
    def GetAllUsers() -> list:
        """Get all the users from the database. Will return an empty list if there are no users."""
        return UserModel.query.all()