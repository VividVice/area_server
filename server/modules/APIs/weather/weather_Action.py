from os import getenv
from sys import path
import callr
path.append('../..')
from modules.database.DB import UserModel
import requests
import time
from os import getenv
from dotenv import load_dotenv

# Actions
# def get_weather():
#     load_dotenv()
#     city = 'Paris'
#     api_key = getenv('WEATHER_API')

#     while True:
#         try:
#             response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}')
#             data = response.json()

#             if 'current' in data and 'weather_descriptions' in data['current']:
#                 current_weather = data['current']['weather_descriptions'][0]
#                 print(f"The current weather in {city} is {current_weather}")

#                 is_sunny = 'sunny' in current_weather.lower()
#                 if is_sunny:
#                     print("It's sunny")
#                 else:
#                     print("It's not sunny")

#         except Exception as e:
#             print(f"Error while getting weather : {e}")

# Reactions
def get_current_weather(user: UserModel, target, city):
    load_dotenv()
    api_key = getenv('WEATHER_API')
    try:
        response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}')
        data = response.json()
        result = ""
        if 'current' in data and 'weather_descriptions' in data['current']:
            current_weather = data['current']['weather_descriptions'][0]
            # "Le temps actuel à {city} est : {current_weather}"
            result += f"The current weather in {city} is {current_weather}"
        else:
            result += "Error while getting weather"

        # send sms
        api = callr.Api(getenv("CALLR_LOGIN"), getenv("CALLR_PASSWORD"))

        sender = "AREACRAFT"

        api.call('sms.send', sender, target, result, None)
        return {"message": "success"}, 200
    except Exception as e:
        return {"message": "anErrorOccured"}, 500