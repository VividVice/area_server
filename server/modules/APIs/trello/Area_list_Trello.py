action_list = [
    {
        "name": "createCard",
        "description": "A new card is created",
        'params': {}
    },
    {
        "name": "createList",
        "description": "A new list is created",
        'params': {}
    },
    {
        "name": "createBoard",
        "description": "A new board is created",
        "params": {}
    },
    {
        "name": "createMember",
        "description": "A new member is added to a board",
        'params': {}
    },
    {
        "name": "updateCard",
        "description": "A card is updated",
        'params': {}
    },
    {
        "name": "updateList",
        "description": "A list is updated",
        'params': {}
    },
    {
        "name": "updateBoard",
        "description": "A board is updated",
        'params': {}
    },
    {
        "name": "updateMember",
        "description": "A member is updated",
        'params': {}
    },
    {
        "name": "deleteCard",
        "description": "A card is deleted",
        'params': {}
    },
    {
        "name": "deleteList",
        "description": "A list is deleted",
        'params': {}
    },
    {
        "name": "deleteBoard",
        "description": "A board is deleted",
        'params': {}
    },
    {
        "name": "deleteMember",
        "description": "A member is deleted",
        'params': {}
    },
]

reactions_list = [
    {
        "name": "createBoard",
        "description": "Creates a board",
        "function_name": "create_board",
        'params': {"name": str}
    },
    {
        "name": "createList",
        "description": "Creates a list",
        "function_name": "create_list",
        'params': {"list_name": str, "board_name": str}
    },
    {
        "name": "createCard",
        "description": "Creates a card",
        "function_name": "create_card",
        'params': {"board_name": str, "list_name": str, "card_name": str}
    },
    {
        "name": "createMember",
        "description": "Adds a member",
        "function_name": "create_member",
        'params': {"name": str, "email": str,} # name is the board name
    },
    {
        "name": "deleteBoard",
        "description": "Deletes a board",
        "function_name": "delete_board",
        'params': {"name": str}
    },
    {
        "name": "deleteList",
        "description": "Deletes a list",
        "function_name": "delete_list",
        'params': {"board_name": str, "list_name": str} # name is the board name
    },
    {
        "name": "undeleteList",
        "description": "Undeletes a list",
        "function_name": "undelete_list",
        'params': {"board_name": str, "list_name": str} # name is the board name
    },
    {
        "name": "deleteCard",
        "description": "Deletes a card",
        "function_name": "delete_card",
        'params': {"board_name": str, "card_name": str}
    },
    {
        "name": "deleteMember",
        "description": "Deletes a member",
        "function_name": "delete_member",
        'params': {"board_name": str, "email": str}
    },
    {
        "name": "updateCard",
        "description": "Updates a card",
        "function_name": "update_card",
        'params': {"board_name": str, "card_name": str, "new_name": str}
    },
    {
        "name": "updateList",
        "description": "Updates a list",
        "function_name": "update_list",
        'params': {"board_name": str, "list_name": str, "new_name": str}
    },
    {
        "name": "updateBoard",
        "description": "Updates a board",
        "function_name": "update_board",
        'params': {"name": str, "new_name": str}
    },
]

