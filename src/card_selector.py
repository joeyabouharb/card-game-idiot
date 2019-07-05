'''
helps validate player card selection and return the appropriate card
'''


def validate_user_input(available_deck: str, user_input: str, user_deck: list,
                        prev_card: dict)-> (int):
    '''
    validates user input to int,
    checks if played card is higher than the prev_card and
    returns the integer as the index of the user deck
    '''
    user_input = user_input.strip()
    if not user_input.isdigit():
        return None
        # val = validate_user_input(
            # input('not a number try again: ', user_deck, prev_card))
    try:
        val = int(user_input) - 1
    except ValueError:
        return None
        # val = validate_user_input(input('please enter a number from 1-3... '))

    if val >= len(user_deck):
        return None
        # val = validate_user_input(
        #    input('please enter a number from 1-3 '), user_deck, prev_card)
    if not check_card_values(available_deck, user_deck, prev_card, val):
        return None
        # val = validate_user_input(
        #    input('please enter a number from 1-3 '), user_deck, prev_card)

    return val


def check_card_values(available_deck: str, user_deck: list, prev_card: dict, val: int)-> (bool):
    '''
    checks the player deck against the previous play,
    if no higher card is found return True or False
    '''
    if available_deck == 'hidden':
        return True
    if user_deck[val]['value'] == 2 or\
        user_deck[val]['value'] == 7 or\
        user_deck[val]['value'] == 10:
        return True
    if not prev_card:
        return True
    if prev_card['value'] == 2 or\
        prev_card['value'] == 10:
        return True

    if user_deck[val]['value'] < prev_card['value']:
        return False
    return True


def get_played_card(user_deck: list, play_card: int)-> (dict):
    '''
    takes in the current user deck as list,
    and the play card which is int
    return's the item dictionary from the user_deck
    '''
    card = user_deck[play_card]
    return card


def validate_multi_input(available_deck: str, val_list: list,\
    user_hand: list, prev_card: dict) -> (list):
    '''
    validate user input
    '''
    if not val_list:
        return False
    if any(val.strip() == '' for val in val_list):
        return False

    if not available_deck == 'hidden':
        index_list = convert_val_list(val_list)
        card_match\
            = check_if_cards_playable(user_hand, index_list, prev_card)
    if not card_match:
        return False 
    is_same_value = check_if_cards_match(user_hand, index_list)
    return index_list if is_same_value else False


def check_if_cards_match(user_hand: list, index_list: list) -> (bool):
    '''
    checks if cards match returns boolean
    '''
    if all(user_hand[index]['value'] == user_hand[index_list[0]]['value'] for index in index_list):
        return True
    return False


def check_if_cards_playable(user_hand: list,\
    index_list: list, prev_card: dict) -> (bool):
    '''
    checks if card is playable
    '''
    if index_list:
        if any(value > len(user_hand) for value in index_list):
            return False
        card_to_match = user_hand[index_list[0]]
        wildcards = [2, 7, 10]
        if card_to_match['value'] in wildcards:
            return True
        if prev_card and\
        card_to_match['value'] < prev_card['value']:
            return False
    return True


def convert_val_list(val_list: list) -> (list):
    '''
    converts string list to int list
    '''
    index_list = []
    for val in val_list:
        if not val.isdigit():
            return False
        num = int(val)
        index_list.append(num - 1)
    duplicates = []
    for iteration in index_list:
        if iteration in duplicates:
            return False
    return index_list
