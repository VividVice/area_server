reactions_list = [
    {
        "name": "postMessageSentiments",
        "description": "Analyse les sentiments d'un message",
        "function_name": "post_message_sentiments",
        'params': {"target": str, "message_content": str}
    },
    {
        "name": "postMessageCategories",
        "description": "Classifie un message en categories",
        "function_name": "post_message_categories",
        'params': {"target": str, "message_content": str}
    },
    {
        "name": "postMessageSummarize",
        "description": "Fait un resumé rapide d'un message",
        "function_name": "post_message_summarize",
        'params': {"target": str, "message_content": str}
    },
    {
        "name": "postMessageMail",
        "description": "Ecrit un mail à partir d'un message",
        "function_name": "post_message_mail",
        'params': {"target": str, "message_content": str}
    }
]
