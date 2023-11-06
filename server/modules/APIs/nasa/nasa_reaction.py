from sys import path
from os import getenv
path.append('../..')
from requests import  get
import webbrowser

# API_NASA = 'IqSMbgDbwtIIl02AfrV0Lu63rMltseXcKSKgh2Hw'

class Nasa():
    @staticmethod
    def get_service_info():
        return {
            "name" : "nasa",
            "reaction" : [
                {
                    "name" : "Daily image",
                    "description" : "A daily image from NASA"
                },
            ]
        }

    @staticmethod
    def get_photo():
        url = f'https://api.nasa.gov/planetary/apod?api_key={getenv("API_NASA")}'
        response = get(url)
        if response.status_code == 200:
            data = response.json()
            image_url = data.get('url')
            return image_url
        else:
            print("Failed to fetch photo. Status code:", response.status_code)


print(Nasa.get_photo())