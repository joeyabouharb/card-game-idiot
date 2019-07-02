'''
This file defines actions user/s can make in order to play the game
'''


def add_to_discard(discard: list, prev_play: dict, player_hand: dict) -> (None):
    '''
    adds played card to discard pile
    '''

    available_hand = get_available_play(player_hand)
    player_hand[available_hand].remove(prev_play)
    discard.insert(0, prev_play)


def get_previous_play(discard: list, index=0) -> (dict):
    '''
    returns previously added cart to discard
    '''
    if not discard:
        return False
    return discard[index] if len(discard) > index else False

def check_user_can_play(player_hand: list, prev_play: dict) -> (bool):
    '''
    if all cards in deck is not greater than the previously played card,
    return False otherwise return True
    '''
    card_checks = []
    wild_cards = [2, 7, 10]
    if not prev_play or\
        any(card['value'] in wild_cards for card in player_hand):
        return False

    for card in player_hand:
        card_checks.append(card['value'] >= prev_play['value'])
    return all(not check for check in card_checks)


def add_discard_to_hand(discard: list, player_hand: list) -> (None):
    '''
    adds discard to player hand
    '''
    player_hand.extend(discard.copy())
    discard.clear()


def get_available_play(user_deck: dict) ->(str):
    '''
    checks what current deck the user could play returns the dictionary
    key -> string
    '''
    if user_deck['user_hand']:
        return 'user_hand'
    elif user_deck['visible']:
        return 'visible'
    return 'hidden'


def check_for_wild_card(current_play: dict)-> (dict):
    '''
    checks for wild card and changes the game execution accordingly
    returns both the new card value and the original as dict
    '''

    is_wildcard = False
    if current_play['value'] == 2\
    or current_play['value'] == 7\
    or current_play['value'] == 10:
        is_wildcard = True

    return is_wildcard


def get_reversed_value(discard: list) -> (dict):
    '''
    get's reversed value when a 7 is played, checks if 7s were played before
    '''
    card_to_match = {}
    if len(discard) > 4:
            cards_to_match = discard[:4]
    else:
            cards_to_match = discard[:len(discard)]
    for card in cards_to_match:
        if card['value'] != 7:
            card_to_match = card
            break
    return card_to_match