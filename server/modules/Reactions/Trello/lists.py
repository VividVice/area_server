import sys
sys.path.append('../')
from modules.APIs.trello.Trello_actions import get_board_data, get_board_members, get_board_lists, get_board_cards

def lists(user, request_data:dict, action_type:str) -> None:
    """Handle the webhook for trello lists."""
    list_id = request_data['action']['data']['list']['id']
    list_name = request_data['action']['data']['list']['name']
    board_id = request_data['action']['data']['board']['id']
    board_name = request_data['action']['data']['board']['name']
    card_id = request_data['action']['data']['card']['id']
    card_name = request_data['action']['data']['card']['name']
    comment = request_data['action']['data']['text']
    if "create" in action_type:
        print('List was created for user: ', user.username, "list name: ", list_name)
    elif "update" in action_type:
        print('List was updated for user: ', user.username, "list name: ", list_name)
    elif "delete" in action_type:
        print('List was deleted for user: ', user.username, "list name: ", list_name)