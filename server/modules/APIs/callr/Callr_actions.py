from os import getenv
from sys import path, stderr
import callr
path.append('../..')
from modules.database.DB import UserModel

# Actions

def create_webhook(user:UserModel, type, endpoint, options):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]
        api = callr.Api(api_login, api_password)
        result = api.call('webhooks.subscribe', type, endpoint, options)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500

def get_webhooks(user:UserModel):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]
        api = callr.Api(api_login, api_password)
        result = api.call('webhooks.get_list')
        return result
    except Exception as e:
        print(e)
        return None

def delete_webhook(user:UserModel, id):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]
        print(api_login, api_password, file=stderr)
        api = callr.Api(api_login, api_password)
        result = api.call('webhooks.unsubscribe', id)
        print(result, file=stderr)
    except Exception as e:
        print(e, file=stderr)
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


def get_list_of_medias(user:UserModel, target):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        result = api.call('media/library.get_list', None)
        print(result)

        sender = "AREACRAFT"
        message = result

        api.call('sms.send', sender, target, message, None)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500


def get_quota_status(user:UserModel, target):
    try:
        user_services = user.user_services["callr"]
        api_login = user_services["username"]
        api_password = user_services["password"]

        print(api_login, api_password)

        api = callr.Api(api_login, api_password)

        result = api.call('did/store.get_quota_status')
        print(result)

        sender = "AREACRAFT"
        message = result

        api.call('sms.send', sender, target, message, None)
    except Exception as e:
        print(e)
        return {"message": "anErrorOccured"}, 500

def get_serice_info():
    return {
        "name" : "callr",
        "actions" : [
            {"name" : "phone_call_recieved", "description" : "Phone call recieved"},
            {"name" : "sms_recieved", "description" : "SMS recieved"},
            {"name" : "media_created", "description" : "Media created"},
            {"name" : "media_updated", "description" : "Media updated"},
            {"name" : "quota_status_updated", "description" : "Quota status updated"}
        ],
        "reactions" : [
            {"name" : "make_call", "description" : "Make a call"},
            {"name" : "send_sms", "description" : "Send a sms"},
            {"name" : "create_media", "description" : "Create a media"},
            {"name" : "update_media_tts", "description" : "Update a media"},
            {"name" : "get_list_of_medias", "description" : "Get a list of medias"},
            {"name" : "get_quota_status", "description" : "Get the quota status"}
        ]
    }