action_list = [
    {
        "name" : "waitTime",
        "description" : "Wait for the timer",
        "function_name": "wait_time",
        "params": {"hour": int, "minute": int}
    },
]

reactions_list = [
    {
        "name": "getCurrentTime",
		"description": "get the current time",
        "function_name": "get_current_time",
		"params": {"continent/city": str}
    },
]