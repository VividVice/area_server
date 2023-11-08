from sys import path
from os import getenv
path.append('../..')
from requests import  get
import callr
from modules.database.DB import UserModel

def get_photo(user: UserModel, target):
    url = f'https://api.nasa.gov/planetary/apod?api_key={getenv("API_NASA")}'
    response = get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data.get('url')
        api = callr.Api(getenv("CALLR_LOGIN"), getenv("CALLR_PASSWORD"))
        sender = "AREACRAFT"
        api.call('sms.send', sender, target, "Here is the nasa image of the day:" + image_url, None)
        return {"message": "success"}, 200

    else:
        return {"message": "anErrorOccured"}, 500

def get_service_info():
    return {
        "name" : "nasa",
        "actions" : [],
        "reactions" : [{"name" : "get_photo", "description" : "Get the photo of the day from nasa and send it as a sms"}]
    }