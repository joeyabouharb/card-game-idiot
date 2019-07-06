'''
This file defines actions user/s can make in order to play the game
'''
from user import send_msg_to_user


def add_to_discard(discard: list, prev_play: dict, player_hand: dict) -> (None):
    '''
    adds played card to discard pile
    '''

    available_hand = get_available_play(player_hand)
    player_hand[available_hand].remove(prev_play)
    discard.insert(0, prev_play)


def get_previous_play(discard: list) -> (dict):
    '''
    returns previously added card to discard
    '''
    if not discard:
        return False
    return discard[0]


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
    if user_deck['visible']:
        return 'visible'
    return 'hidden'


def check_for_wild_card(current_play: dict)-> (bool):
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


def end_game(user_deck: dict, opponent_deck: dict, is_human: bool, name: str):
    '''
    handles end game by saving the game score in file
    '''
    score = 0
    if is_human:
        score = len(opponent_deck['user_hand']) +\
                len(opponent_deck['visible']) + \
                len(opponent_deck['hidden'])
    else:
        score = len(user_deck['user_hand']) -\
                len(user_deck['visible']) -\
                len(user_deck['hidden'])
    data = {
        "name": name,
        "score": score
    }
    return data


def get_next_turn(is_human: bool, user_deck: dict,\
    opponent_deck: dict) -> (dict, dict, bool):
    '''
    get's the next turn in game
    '''
    is_human = not is_human
    deck = user_deck if is_human else opponent_deck
    opponent_deck = opponent_deck if is_human else user_deck
    opponent_stats = {
        "cards_in_hand": len(opponent_deck['user_hand']),
        "visible": opponent_deck['visible']
    }
    return deck, opponent_stats, is_human


def stringify_result(result: dict) -> (str):
    '''
    returns result as string to display to user
    '''
    return (
        "final score: \n"
        f'Name:{result["name"]}\n'
        f'Score:{result["score"]}'
    )


def check_if_game_ended(user_deck: dict, opponent_deck: dict) -> (bool):
    '''
    checks if cards have been exhausted from both player decks
    '''
    return (
        all(not filled for filled in user_deck.values()) or
        all(not filled for filled in opponent_deck.values())
    )

def check_four_of_a_kind(discard: list) -> (bool):
    '''
    check's if there was a 4 of a kind play, bombs the deck
    '''
    if len(discard) < 4:
        return False

    card_set = discard[:4]
    prev_card = get_previous_play(discard)
    if all(card['value'] == prev_card['value'] for card in card_set):
        send_msg_to_user('Four of a kind! deck bombed!')
        return True
