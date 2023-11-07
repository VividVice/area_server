from sys import path, stderr
from os import getenv
path.append('../..')
from modules.database.DB import UserModel
from requests import  get, post, delete, put

# make a obj requst that has the method get from requests

def get_service_info():
    return {
        "name" : "trello",
        "actions" : [
            {
                "name" : "new_card",
                "description" : "A new card is created"
            },
            {
                "name" : "new_list",
                "description" : "A new list is created"
            },
            {
                "name" : "new_board",
                "description" : "A new board is created"
            },
            {
                "name" : "new_member",
                "description" : "A new member is added to a board"
            },
            {
                "name" : "card updated",
                "description" : "A card is updated"
            },
            {
                "name" : "list updated",
                "description" : "A list is updated"
            },
            {
                "name" : "board updated",
                "description" : "A board is updated"
            },
            {
                "name" : "member updated",
                "description" : "A member is updated"
            },
            {
                "name" : "card deleted",
                "description" : "A card is deleted"
            },
            {
                "name" : "list deleted",
                "description" : "A list is deleted"
            },
            {
                "name" : "board deleted",
                "description" : "A board is deleted"
            },
            {
                "name" : "member deleted",
                "description" : "A member is deleted"
            },
        ],
        "reactions" : [
            {"name": "Create a board", "description": "Creates a board"},
            {"name": "Create a list", "description": "Creates a list"},
            {"name": "Create a card", "description": "Creates a card"},
            {"name": "Add a member", "description": "Adds a member"},
            {"name": "Delete a board", "description": "Deletes a board"},
            {"name": "Delete a list", "description": "Deletes a list"},
            {"name": "Delete a card", "description": "Deletes a card"},
            {"name": "Delete a member", "description": "Deletes a member"},
            {"name": "Update a board", "description": "Updates a board"},
            {"name": "Update a list", "description": "Updates a list"},
            {"name": "Update a card", "description": "Updates a card"},
            {"name": "Update a member", "description": "Updates a member"}
        ]
    }

def get_user_id(user:UserModel):
    url = f"https://api.trello.com/1/members/me"
    response = get(url, headers= create_auth_header(user))
    return response.json()["id"]

def create_auth_header(user:UserModel):
    header = f'OAuth oauth_consumer_key="{getenv("API_TRELLO")}"'
    print(user.user_services)
    header += f', oauth_token="{user.user_services["trello"]["access_token"]}"'
    return {"Authorization": header}

def get_user_boards(user:UserModel):
    url = "https://api.trello.com/1/members/me/boards"
    response = get(url, headers= create_auth_header(user))
    return response.json()

def get_other_user_id(user:UserModel, email):
    url = f"https://api.trello.com/1/members/{email}"
    response = get(url, headers= create_auth_header(user))
    return response.json()["id"]

def get_board_id(user:UserModel, name):
    boards = get_user_boards(user)
    for board in boards:
        if board["name"] == name:
            return board["id"]
    return None

def get_board_data(user:UserModel, name):
    boards = get_user_boards(user)
    for board in boards:
        if board["name"] == name:
            return board
    return None

def get_board_lists(user:UserModel, name):
    board_id = name
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    response = get(url, headers= create_auth_header(user))
    return response.json()

def get_board_cards(user:UserModel, name):
    board_id = get_board_id(user, name)
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    response = get(url, headers= create_auth_header(user))
    cards = response.json()
    card_dict = {card['name']: card['id'] for card in cards}
    return card_dict

def get_board_members(user:UserModel, name):
    board_id = get_board_id(user, name)
    url = f"https://api.trello.com/1/boards/{board_id}/members"
    response = get(url, headers= create_auth_header(user))
    members = response.json()
    member_dict = {member['username']: member['id'] for member in members}
    return member_dict

# create methods
def create_board(user:UserModel, name):
    url = f"https://api.trello.com/1/boards/"
    response = post(url, headers= create_auth_header(user), data={"name": name})

def create_list(user:UserModel, board_name, list_name):
    board_id = get_board_id(user, board_name)
    url = f"https://api.trello.com/1/lists"
    response = post(url, headers= create_auth_header(user), data={"name": list_name, "idBoard": board_id})

def create_card(user: UserModel, board_name, list_name, card_name):
    board_id = get_board_id(user, board_name)
    lists = get_board_lists(user, board_id)
    list_id = list(filter(lambda x: x["name"] == list_name, lists))[0]["id"]
    url = f"https://api.trello.com/1/cards"
    response = post(url, headers=create_auth_header(user), data={"idList": list_id,"desc": card_name})

def create_member(user:UserModel, name, email):
    url = f"https://api.trello.com/1/boards/{get_board_id(user, name)}/members"
    response = put(url, headers= create_auth_header(user), data={"email": email})


# update methods
def update_board(user:UserModel, name, new_name):
    url = f"https://api.trello.com/1/boards/{get_board_id(user, name)}"
    response = put(url, headers= create_auth_header(user), data={"name": new_name})

#done
def update_list(user:UserModel, board_name, list_name, new_name):
    board_id = get_board_id(user, board_name)
    list_id = get_board_lists(user, board_id)
    url = f"https://api.trello.com/1/lists/{list_id}"
    response = put(url, headers= create_auth_header(user))

# def update_card(user:UserModel, board_name, card_name, new_name):
#     board_cards = get_board_cards(user, board_name)

def update_card(user:UserModel, board_name, card_name, new_name):
    board_cards = get_board_cards(user, board_name)
    card_id = board_cards[card_name]
    url = f"https://api.trello.com/1/cards/{card_id}"
    response = put(url, headers=create_auth_header(user), data={"name": new_name})


# delete methods
def delete_board(user:UserModel, name):
    url = f"https://api.trello.com/1/boards/{get_board_id(user, name)}"
    response = delete(url, headers= create_auth_header(user))
#done
def delete_list(user:UserModel, board_name, list_name):
    board_id = get_board_id(user, board_name)
    list_id = get_board_lists(user, board_id)
    url = f"https://api.trello.com/1/lists/{list_id}/closed"
    response = put(url, headers= create_auth_header(user), data={"value": "true"})

def undelete_list(user:UserModel, board_name, list_name):
    board_id = get_board_id(user, board_name)
    list_id = get_board_lists(user, board_id)
    url = f"https://api.trello.com/1/lists/{list_id}/closed"
    response = put(url, headers= create_auth_header(user), data={"value": "false"})

#done
def delete_card(user:UserModel, board_name, card_name):
    board_cards = get_board_cards(user, board_name)
    card_id = board_cards[card_name]
    url = f"https://api.trello.com/1/cards/{card_id}"
    response = delete(url, headers= create_auth_header(user))

def delete_member(user:UserModel, board_name, email):
    url = f"https://api.trello.com/1/boards/{get_board_id(user, board_name)}/members/{get_other_user_id(user, email)}"
    response = delete(url, headers= create_auth_header(user))

# webhook methods
def get_webhooks_for_user(user:UserModel):
    url = f"https://api.trello.com/1/tokens/{user.user_services['trello']['access_token']}/webhooks/?key={getenv('API_TRELLO')}"
    response = get(url, headers= create_auth_header(user))
    return response.status_code == 200

def delete_webhook(user:UserModel, webhook_id):
    url = f"https://api.trello.com/1/webhooks/{webhook_id}"
    response = delete(url, headers= create_auth_header(user))
    return response.status_code == 200


def post_webhook(user:UserModel, webhook_data):
    url = f"https://api.trello.com/1/tokens/{user.user_services['trello']['access_token']}/webhooks/?key={getenv('API_TRELLO')}"
    response = post(url, json=webhook_data, headers={"Content-Type": "application/json"})
    print("status code", response.status_code)
    return response.status_code == 200