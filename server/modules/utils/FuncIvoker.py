import sys
sys.path.append('../')
from modules.APIs.trello.Trello_actions import *
from modules.APIs.callr.Callr_actions import *
from modules.APIs.chatgpt.ChatGPT_actions import *
from modules.APIs.timer.time_action import *
from modules.APIs.weather.weather_Action import *
from server.modules.APIs.nasa.nasa_action import *

# using a name of fuction given as a string call it and pass the params to it (if any) you must unpack the params first, params are
# given as args to the function so use kwargs(the equviant to args_list in C) to unpack them
# example:user = DB.GetUser(payload["username"])
# FuncInvoker('my_function', user=user, **reaction_dict["params"])

list_of_reactions = {
    "trello" : [
        {"create_card" : create_card},
        {"create_list" : create_list},
        {"create_board" : create_board},
        {"create_member" : create_member},
        {"update_card" : update_card},
        {"update_list" : update_list},
        {"update_board" : update_board},
        {"delete_card" : delete_card},
        {"delete_list" : delete_list},
        {"undelete_list" : undelete_list},
        {"delete_board" : delete_board},
        {"delete_member" : delete_member}
    ],
    "callr" : [
        {"make_call": make_call},
        {"send_sms": send_sms},
        {"create_media": create_media},
        {"update_media_tts": update_media_tts},
        {"get_list_of_medias": get_list_of_medias},
        {"get_quota_status": get_quota_status}
    ],
    "chatgpt" : [
        {"post_message_sentiments": post_message_sentiments},
        {"post_message_categories": post_message_categories},
        {"post_message_summarize": post_message_summarize},
        {"post_message_mail": post_message_mail}
    ],
    "time" : [
        {"get_current_time": get_current_time}
    ],
    "weather" : [
        {"get_current_weather": get_current_weather}
    ],
    "nasa" : [
        {"get_photo": get_photo}
    ],
}

def FuncInvoker(service_name, func_name, user, **kwargs):
    # get the function to call
    try :
        func = list(filter(lambda x: list(x.keys())[0] == func_name, list_of_reactions[service_name]))[0][func_name]
    except Exception:
        raise Exception(f"Function {func_name} not found in service {service_name}")
    return func(user=user, **kwargs)