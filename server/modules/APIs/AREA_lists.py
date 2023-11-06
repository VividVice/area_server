import sys
sys.path.append('../../')
from modules.APIs.trello.Area_list_Trello import action_list as trello_ac, reactions_list as trello_re
from modules.APIs.callr.AREA_list_Callr import action_list as callr_ac, reactions_list as callr_re
from modules.APIs.trello.TrelloWebhook import Setup as trello_setup
from modules.APIs.callr.Callr_Webhook import Setup as callr_setup
from modules.APIs.chatgpt.AREA_list_ChatGPT import reactions_list as chatgpt_re
from modules.APIs.timer.AREA_list_Timer import reactions_list as time_re
from modules.APIs.weather.AREA_list_Weather import reactions_list as weather_re

action_list = {
    "trello": trello_ac,
    "callr": callr_ac,
}

setup_methods = {
    "trello": trello_setup,
    "callr": callr_setup,
}

reaction_list = {
    "trello": trello_re,
    "callr": callr_re,
    "chatgpt": chatgpt_re,
    "time": time_re,
    "weather": weather_re,
}

"""
   "reaction_params": {
        "name: str,
        "id" : int
    }
"""

def Create_Area(user, action_name : str,
                action_params : str, action_service : str,
                reaction_name: str, reaction_params: str,
                reaction_service: str):
    from modules.database.DB import DataBaseOpps as DB
    """
    it needs to either create a webhook for the action or if it was created for different reaction just add
    the reaction to the webhook to that end we must save the action and a list of reactions that are dependent on it with their arguments
    the schema should look like this:
    User.user_args = {
        ...other_services
        "trello" : {
            "access_token": str, # specific to the service Trello in this case other service may use different things
            # the field below will be there for all services
            "Areas": [{ "action": str, "subbed_reactions": [{"service_name": str, "reaction_name": str,"function_name" : str, params: {"arg_name": "arg_value", ...}}]}]
        }
    }
    the first Area of each user will have Areas = []
    """
    service_args = DB.getServiceArgs(user, action_service)
    # get the function to call for the reaction
    reaction_function = list(filter(lambda x: x["name"] == reaction_name, reaction_list[reaction_service]))[0]["function_name"]
    # checks if the actions is already in the Areas if it is then add the reaction to it (even if it is a duplicate for that action)
    for area in service_args["Areas"]:
        if area["action"] == action_name:
            area["subbed_reactions"].append({
                "service_name": reaction_service,
                "reaction_name": reaction_name,
                "function_name": reaction_function,
                "params": reaction_params
            })
            # update the database
            user.user_services[action_service] = service_args
            DB.Commit()
            return
    # # if it is not then create a webhook and then add the info to the Areas also do this if the list is empty
    setup_methods[action_service](user, action_name, action_params)
    service_args["Areas"].append({
        "action": action_name,
        "subbed_reactions": [{
            "service_name": reaction_service,
            "reaction_name": reaction_name,
            "function_name": reaction_function,
            "params": reaction_params
        }]
    })
    user.user_services[action_service] = service_args
    # update the database
    DB.Commit()
