import sys
sys.path.append('../')
from modules.APIs.trello.Trello_actions import get_card_data, get_card_members, get_card_labels, get_card_comments, get_card_attachments, get_card_checklists
from modules.database.DB import DataBaseOpps as DB

def cards(user, request_data, action_type):
    card_id = request_data['action']['data']['card']['id']
    card_name = request_data['action']['data']['card']['name']
    card_url = request_data['action']['data']['card']['url']
    # card_data =  get_card_data(user, card_id)
    # card_members =  get_card_members(user, card_id)
    # card_labels =  get_card_labels(user, card_id)
    # card_comments =  get_card_comments(user, card_id)
    # card_attachments =  get_card_attachments(user, card_id)
    # card_checklists =  get_card_checklists(user, card_id)
    if action_type == 'createCard':
        print('Card was created for user: ', user.username, "card name: ", card_name)
    elif action_type == 'updateCard':
        print('Card was updated for user: ', user.username, "card name: ", card_name)
    elif action_type == 'deleteCard':
        print('Card was deleted for user: ', user.username, "card name: ", card_name)
    else:
        return {'message': 'unknown action type'}, 400
