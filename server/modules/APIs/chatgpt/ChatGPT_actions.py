from sys import path, stderr
from os import getenv
import json
import callr
import requests
path.append('../..')
from modules.config.config import Config
from modules.database.DB import UserModel
from requests import  get, post, delete, put

def create_auth_header(user: UserModel):
    header = {
        "Content-Type": "application/json",
        "api-key": getenv("CHATGPT_API_KEY")
    }
    return header

def get_service_info():
    return {
        "name" : "chatgpt",
        "actions" : [],
        "reactions" : [
            {"name" : "post_message", "description" : "Post a message to a phone number"},
            {"name" : "post_message_sentiments", "description" : "Post a message to a phone number"},
            {"name" : "post_message_categories", "description" : "Post a message to a phone number"},
            {"name" : "post_message_summarize", "description" : "Post a message to a phone number"},
            {"name" : "post_message_mail", "description" : "Post a message to a phone number"}
        ]
    }

def post_message_sentiments(user: UserModel, target, message_content):
    url = "https://luna-aibot-demo-oai.openai.azure.com/openai/deployments/WidgetFaces/chat/completions?api-version=2023-07-01-preview"
    data = {
        "messages": [
            {"role": "user", "content": "Analyse les sentiments du message suivant:" + message_content},
        ],
        "max_tokens": 300,
        "temperature": 0.7,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "top_p": 0.95,
        "stop": None
    }
    response = post(url, headers=create_auth_header(user), data=json.dumps(data))
    print(extract_response_message(response.json()), file=stderr)

    # send sms

    api = callr.Api(getenv("CALLR_LOGIN"), getenv("CALLR_PASSWORD"))

    sender = "AREACRAFT"
    message = extract_response_message(response.json())

    api.call('sms.send', sender, target, message, None)
    return extract_response_message(response.json())

def post_message_categories(user: UserModel, target, message_content):
    url = "https://luna-aibot-demo-oai.openai.azure.com/openai/deployments/WidgetFaces/chat/completions?api-version=2023-07-01-preview"
    data = {
        "messages": [
            {"role": "user", "content": "classifie ce texte en categories du message suivant:" + message_content},
        ],
        "max_tokens": 300,
        "temperature": 0.7,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "top_p": 0.95,
        "stop": None
    }
    response = post(url, headers=create_auth_header(user), data=json.dumps(data))
    print(extract_response_message(response.json()), file=stderr)

    # send sms
    api = callr.Api(getenv("CALLR_LOGIN"), getenv("CALLR_PASSWORD"))

    sender = "AREACRAFT"
    message = extract_response_message(response.json())

    api.call('sms.send', sender, target, message, None)
    return extract_response_message(response.json())

def post_message_summarize(user: UserModel, target, message_content):
    url = "https://luna-aibot-demo-oai.openai.azure.com/openai/deployments/WidgetFaces/chat/completions?api-version=2023-07-01-preview"
    data = {
        "messages": [
            {"role": "user", "content": "fait un resumé rapide du message suivant:" + message_content},
        ],
        "max_tokens": 300,
        "temperature": 0.7,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "top_p": 0.95,
        "stop": None
    }
    response = post(url, headers=create_auth_header(user), data=json.dumps(data))
    print(extract_response_message(response.json()), file=stderr)

    # send sms
    api = callr.Api(getenv("CALLR_LOGIN"), getenv("CALLR_PASSWORD"))

    sender = "AREACRAFT"
    message = extract_response_message(response.json())

    api.call('sms.send', sender, target, message, None)
    return extract_response_message(response.json())

def post_message_mail(user: UserModel, target, message_content):
    url = "https://luna-aibot-demo-oai.openai.azure.com/openai/deployments/WidgetFaces/chat/completions?api-version=2023-07-01-preview"
    data = {
        "messages": [
            {"role": "user", "content": "ecrit un mail à partir du message suivant:" + message_content},
        ],
        "max_tokens": 300,
        "temperature": 0.7,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "top_p": 0.95,
        "stop": None
    }
    response = post(url, headers=create_auth_header(user), data=json.dumps(data))
    print(extract_response_message(response.json()), file=stderr)

    # send sms
    api = callr.Api(getenv("CALLR_LOGIN"), getenv("CALLR_PASSWORD"))

    sender = "AREACRAFT"
    message = extract_response_message(response.json())

    api.call('sms.send', sender, target, message, None)
    return extract_response_message(response.json())

def extract_response_message(response_json):
    bot_response = response_json["choices"][0]["message"]["content"]
    return bot_response

# Usage Example
# Assuming you have a UserModel instance called user
# chat_gpt = ChatGPT()
# response_json = chat_gpt.post_message(user, "Hello, how are you?")
# response_message = chat_gpt.extract_response_message(response_json)
# print(response_message)
