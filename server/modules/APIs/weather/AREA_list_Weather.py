action_list = [
    {
        "name" : "getWeather",
        "description" : "Get the current weather",
        "function_name": "get_weather",
        "params": {}
    },
]

reactions_list = [
    {
        "name": "getCurrentWeather",
        "description": "Get the current weather",
        "function_name": "get_current_weather",
        "params": {"target": str, "city": str}
    },
]