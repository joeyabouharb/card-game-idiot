'''
This file defines actions user/s can make in order to play the game
'''


def add_to_discard(discard: list, prev_play: dict, player_hand: list) -> (None):
    '''
    adds played card to discard pile
    '''
    available_hand = get_available_play(player_hand)
    player_hand[available_hand].remove(prev_play)
    discard.insert(0, prev_play)
    print(discard)

def get_previous_play(discard: list) -> (dict):
    '''
    returns previously added cart to discard
    '''
    if not discard:
        return {'value': 0}
    return discard[0]

def check_user_can_play(player_hand: list, prev_play: dict) -> (bool):
    '''
    if all cards in deck is not greater than the previously played card,
    return False otherwise return True
    '''
    card_checks = []
    wild_cards = [2, 7, 10]
    if not prev_play['value'] or\
        any(card['value'] in wild_cards for card in player_hand):
        return False

    for card in player_hand:
        card_checks.append(card['value'] > prev_play['value'])
    print(player_hand)
    print(card_checks)
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
    if user_deck['user_hand'] is not False:
        return 'user_hand'
    if user_deck['visible'] is not False:
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
