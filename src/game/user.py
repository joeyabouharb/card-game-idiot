'''
module to handle user turn
'''
from actions import validate_user_input,\
    get_previous_play,\
    get_played_card,\
    check_for_wild_card


def stringify_deck(user_deck: dict) -> (str):
    '''
    grabs user's current hand and  ->
    returns strings
    '''
    msg = "user's current Hand:\n"
    
    for i, card in enumerate(user_deck['user_hand']):
        i += 1
        msg += f'{i} {card}'


def prompt_user_turn(user_deck: dict, discard: list) -> (dict):
    '''
    prompt user turn returns the selected card as dict
    '''
    prev_card = get_previous_play(discard)

    user_view = stringify_deck(user_deck)
    print(user_view)

    user_input = None
    while user_input is None:
        user_input = input('')

    index = validate_user_input(user_deck, prev_card)
    current_play = get_played_card(user_deck, index)
    return check_for_wild_card(True, prev_card, current_play, discard)


