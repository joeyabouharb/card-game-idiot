'''
This file defines actions user/s can make in order to play the game
'''


def validate_user_input(user_input: str, user_deck: list,
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


    if not check_card_values(user_deck, prev_card, val):
        return None
        # val = validate_user_input(
        #    input('please enter a number from 1-3 '), user_deck, prev_card)

    return val


def get_played_card(user_deck: list, play_card: int)-> (dict):
    '''
    takes in the current user deck as list,
    and the play card which is int
    return's the item dictionary from the user_deck
    '''
    card = user_deck[play_card]
    return card


def check_card_values(user_deck: list, prev_card: dict, val: int)-> (bool):
    '''
    checks the player deck against the previous play,
    if no higher card is found return True or False
    '''
    if user_deck[val]['value'] == 2 or\
        user_deck[val]['value'] == 7 or\
        user_deck[val]['value'] == 10:
        return True

    if user_deck[val]['value'] < prev_card['value']:
        return False
    return True


def add_to_discard(discard: list, prev_play: dict) -> (None):
    '''
    adds played card to discard pile
    '''
    discard.insert(0, prev_play)


def get_previous_play(discard: list) -> (dict):
    '''
    returns previously added cart to discard
    '''
    return discard[0]

def check_user_can_play(player_hand: list, prev_play: dict) -> (bool):
    '''
    if all cards in deck is not greater than the previously played card,
    return False otherwise return True
    '''
    card_checks = []
    for card in player_hand:
        card_checks.append(card['value'] > prev_play['value'])
    return all(check is False for check in card_checks)

def add_discard_to_hand(discard: list, player_hand: list) -> (None):
    '''
    adds discard to player hand
    '''
    player_hand.extend(discard.copy())
    discard = []


def check_for_wild_card(is_human: bool, prev_play: dict,
                        current_play: dict, discard: list)-> (dict):
    '''
    checks for wild card and changes the game accordingly
    '''

    if current_play['value'] == 2:
        current_play['value'] = 0
    elif current_play['value'] == 7:
        current_play['value'] = prev_play['value']
    elif current_play['value'] == 10:
        discard.clear()
        return None
    return current_play
