'''
module to define AI behaviour
'''
import random
from operator import (
    itemgetter
)
from card_selector import (
    get_played_card,
    check_card_values
)


def prompt_opponent_turn(available_deck: str, opponent_deck: dict,\
        prev_card: dict, opponent_stats: dict, wildcard={}):
    '''
    handles opponent turn and card selection
    '''

    random_number = generate_random_number(1, 10)
    playable_deck = opponent_deck[available_deck]
    sorted_deck = sorted(playable_deck, key=itemgetter('value'))
    is_valid = False
    while not is_valid:
        index = select_choice_from_random(random_number, sorted_deck, prev_card)
        is_valid = check_card_values(available_deck, sorted_deck, prev_card, index)

    played_card = get_played_card(sorted_deck, index)

    return played_card

def generate_random_number(value_a: int, value_b: int) -> (int):
    '''
    generates a random number in order to define AI behaviour
    returns int
    '''
    return random.randrange(value_a, value_b)


def select_choice_from_random(random_number: int, playable_deck: list, prev_card: dict) -> (int):
    '''
    returns selected index from random_number
    '''
    if random_number < 6:
        index = select_randomly(playable_deck)
    elif random_number >=6 and\
    random_number < 10:
        index = select_an_ok_choice(playable_deck, prev_card)
    return index


def select_randomly(sorted_deck: list):
    return random.choice(range(len(sorted_deck)))


def select_an_ok_choice(sorted_deck: list, prev_card: dict):
    '''
    
    '''
    selected_index = None
    if not prev_card:
        prev_card  = {"value": 0}
    for i, card in enumerate(sorted_deck):
        if card['value'] >= prev_card['value']:
            selected_index = i
            break
    if selected_index is None:
        value_list = [card['value'] for card in sorted_deck]
        if value_list.count(2) > 0:
            selected_index = value_list.index(2)
        elif value_list.count(10) > 0:
            selected_index = value_list.index(10)
        elif value_list.count(7):
            selected_index = value_list.index(7)
    return selected_index