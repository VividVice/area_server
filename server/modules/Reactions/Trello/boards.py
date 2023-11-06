import sys
sys.path.append('../')
from modules.APIs.trello.Trello_actions import get_board_data, get_board_members, get_board_lists, get_board_cards

def boards(user, request_data, action_type):
    board_id = request_data['action']['data']['board']['id']
    board_name = request_data['action']['data']['board']['name']
    board_url = request_data['action']['data']['board']['url']
    board_data =  get_board_data(user, board_id)
    board_members =  get_board_members(user, board_id)
    board_lists =  get_board_lists(user, board_id)
    board_cards =  get_board_cards(user, board_id)
    if action_type == 'createBoard':
        print('Board was created for user: ', user.username, "board name: ", board_name)
    elif action_type == 'updateBoard':
        print('Board was updated for user: ', user.username, "board name: ", board_name)
    elif action_type == 'deleteBoard':
        print('Board was deleted for user: ', user.username, "board name: ", board_name)