from os import getenv
from sys import path
path.append('../..')
from modules.database.DB import UserModel
import requests
import callr
import time
from os import getenv
from dotenv import load_dotenv

# Actions
# def wait_time(target_hour, target_minute):
#     try:
#         while True:
#             response = requests.get("http://worldtimeapi.org/api/ip")
#             data = response.json()
#             current_hour = int(data['datetime'][11:13])
#             current_minute = int(data['datetime'][14:16])

#             if current_hour == target_hour and current_minute == target_minute:
#                 print("Hello")
#                 break

#             time.sleep(2)
#     except Exception as e:
#         print(f"Erreur lors de la récupération de l'heure : {e}")

# Reactions
def get_current_time(user: UserModel, target, city):
    url = f'http://worldtimeapi.org/api/timezone/{city}'

    try:
        response = requests.get(url)
        data = response.json()
        result = ""
        current_time = data['datetime']
        current_time = current_time.split('T')[1]
        result += f"L'heure actuelle à {city} est : {current_time}"

        api = callr.Api(getenv("CALLR_LOGIN"), getenv("CALLR_PASSWORD"))

        sender = "AREACRAFT"

        api.call('sms.send', sender, target, result, None)
        return {"message": "success"}, 200
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return {"message": "anErrorOccured"}, 500
