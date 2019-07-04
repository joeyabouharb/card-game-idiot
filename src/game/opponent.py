'''
module to define AI behaviour
'''
import random
from operator import (
    itemgetter
)
from .card_selector import (
    get_played_card,
    check_card_values
)


def prompt_opponent_turn(available_deck: str, opponent_deck: dict,\
        prev_card: dict, opponent_stats: dict, wildcard={}):
    '''
    handles opponent turn and card selection
    '''
    enemy_is_winning = True if not opponent_stats['cards_in_hand'] else False
    random_number = generate_random_number(1, 10)
    playable_deck = opponent_deck[available_deck]
    sorted_deck = sorted(playable_deck, key=itemgetter('value'))
    is_valid = False
    while not is_valid:
        index = select_choice_from_random(random_number, sorted_deck, prev_card, enemy_is_winning)
        is_valid = check_card_values(available_deck, sorted_deck, prev_card, index)

    played_card = get_played_card(sorted_deck, index)
    if played_card['value'] == 10:
        print(f'{played_card["name"]}')
    return played_card

def generate_random_number(value_a: int, value_b: int) -> (int):
    '''
    generates a random number in order to define AI behaviour
    returns int
    '''
    return random.randrange(value_a, value_b)


def select_choice_from_random(random_number: int, playable_deck: list,\
    prev_card: dict, enemy_is_winning: bool) -> (int):
    '''
    returns selected index from random_number
    '''
    if random_number < 6:
        index = select_randomly(playable_deck)
    elif random_number >=6 and\
    random_number < 10:
        index = select_an_ok_choice(playable_deck, prev_card, enemy_is_winning)
    return index


def select_randomly(sorted_deck: list):
    return random.choice(range(len(sorted_deck)))


def select_an_ok_choice(sorted_deck: list, prev_card: dict, enemy_is_winning: bool):
    '''
    let the AI select a decent play
    '''
    selected_index = None
    if enemy_is_winning: # play high if enemy is winning
        sorted_deck.reverse()
        selected_index = 0
    else: # play safe, play lowest possible card
        for i, card in enumerate(sorted_deck):
            if not prev_card or card['value'] >= prev_card['value']:
                selected_index = i
                break
        if selected_index is None: # else play other wildcards if no higher card is found
            value_list = [card['value'] for card in sorted_deck]
            if value_list.count(7) > 0:
                selected_index = value_list.index(7)
            elif value_list.count(10) > 0:
                selected_index = value_list.index(10)
            elif value_list.count(2):
                selected_index = value_list.index(2)
    return selected_index