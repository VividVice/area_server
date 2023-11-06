import sys
sys.path.append('../')
from modules.APIs.trello.Trello_actions import get_member_data, get_member_boards, get_member_cards, get_member_actions

def members(user, request_data, action_type):
    member_id = request_data['action']['memberCreator']['id']
    member_name = request_data['action']['memberCreator']['fullName']
    member_username = request_data['action']['memberCreator']['username']
    member_data =  get_member_data(user, member_id)
    member_boards =  get_member_boards(user, member_id)
    member_cards =  get_member_cards(user, member_id)
    member_actions =  get_member_actions(user, member_id)
    if action_type == 'addMemberToBoard':
        print('Member was added to board for user: ', user.username, "member name: ", member_name)
    elif action_type == 'removeMemberFromBoard':
        print('Member was removed from board for user: ', user.username, "member name: ", member_name)
    else:
        return {'message': 'unknown action type'}, 400