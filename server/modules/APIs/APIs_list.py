import sys
sys.path.append("..")
from modules.APIs.service_supcription.StrategySubcrpition import SubscriptionStrategy, UnSubscriptionStrategy
from modules.APIs.service_supcription.TestStrategy import TestSubcrpibeStrategy, TestUnSubcrpibeStrategy
from modules.APIs.trello.TrelloSubStrat import TrelloSubStrat, TrelloUnSubStrat
from modules.APIs.callr.Callr_strategy import CallrSubStrategy, CallrUnsubStrategy
from modules.APIs.github.Github_substract import GithubSubStrat, GithubUnSubStrat
from modules.APIs.timer.time_strategie import TimerSubstrtegy, TimerUnsubStrategy
from modules.APIs.weather.weather_strategie import WeatherSubstrtegy, WeatherUnsubStrategy
from modules.APIs.chatgpt.ChatGPT_strategy import ChatGPTSubStrategy, ChatGPTUnsubStrategy
""" Key = service name , value =
    {
        "subscribe" : subscribe strategy,
        "unsubscribe" : unsubscribe strategy
    }
"""
list_api = {
    "testSub" : {
        "subscribe" : TestSubcrpibeStrategy(),
        "unsubscribe" : TestUnSubcrpibeStrategy()
    },
    "trello" : {
        "subscribe" : TrelloSubStrat(),
        "unsubscribe" : TrelloUnSubStrat()
    },
    "github" : {
        "subscribe" : GithubSubStrat(),
        "unsubscribe" : GithubUnSubStrat()
    },
    "callr" : {
        "subscribe" : CallrSubStrategy(),
        "unsubscribe" : CallrUnsubStrategy()
    },
    "time" : {
        "subscribe" : TimerSubstrtegy(),
        "unsubscribe" : TimerUnsubStrategy()
    },
    "weather" : {
        "subscribe" : WeatherSubstrtegy(),
        "unsubscribe" : WeatherUnsubStrategy()
    },
    "chatgpt" : {
        "subscribe" : ChatGPTSubStrategy(),
        "unsubscribe" : ChatGPTUnsubStrategy()
    }
}