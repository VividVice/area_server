from os import getenv
from sys import path
import callr
path.append('../..')
from modules.database.DB import UserModel

# Actions

def create_webhook(user:UserModel, type, endpoint, options):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]
        print(api_login, api_password)
        api = callr.Api(api_login, api_password)
        result = api.call('webhooks.create', type, endpoint, options)
        print(result)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500

# Reactions

def make_call(user:UserModel, target, msg):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        target = {
            'number': target,
            'timeout': 30
        }

        if msg == '':
            msg = 'Hello world! how are you ? I hope you enjoy this call. good bye.'

        messages = [131, 132, 'TTS|TTS_EN-GB_SERENA|' + msg]

        options = {
            'cdr_field': 'userData',
            'cli': 'BLOCKED',
            'loop': 2
        }

        result = api.call('calls.broadcast_1', target, messages, options)
        print(result)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500


def send_sms(user:UserModel, target, msg, sender):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        if sender == '':
            sender = 'SMS'

        result = api.call('sms.send', sender, target, msg, None)
        print(result)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500


def create_media(user:UserModel, name):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        result = api.call('media/library.create', name)
        print(result)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500


def update_media_tts(user:UserModel, id, msg):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        # example media_id = 6869741

        result = api.call('media/tts.set_content', id, msg, 'TTS_EN-GB_SERENA', None)
        print(result)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500


def get_list_of_medias(user:UserModel):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        result = api.call('media/library.get_list', None)
        print(result)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500


def get_quota_status(user:UserModel):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        result = api.call('did/store.get_quota_status')
        print(result)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500
