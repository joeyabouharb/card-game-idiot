'''
module to define AI behaviour
'''
import random
from user import send_msg_to_user
from operator import (
    itemgetter
)
from card_selector import (
    get_played_card,
    check_card_values
)


def prompt_opponent_turn(
    available_deck: str,
    opponent_deck: dict,
    prev_card: dict,
    opponent_stats: dict,
    wildcard=False
) -> (dict):
    '''
    handles opponent turn and card selection
    '''
    if wildcard:
        send_msg_to_user(
            f'wildcard played! {wildcard["name"]}'
        )
    enemy_is_winning =\
        bool(
            not opponent_stats['cards_in_hand']
        )
    random_number =\
        generate_random_number(1, 10)
    playable_deck =\
        opponent_deck[available_deck]
    sorted_deck =\
        sorted(
            playable_deck,
            key=itemgetter('value')
        )
    is_valid = False

    while not is_valid:
        index =\
            select_choice_from_random(
                available_deck,
                random_number,
                sorted_deck,
                prev_card,
                enemy_is_winning
            )
        is_valid =\
            check_card_values(
                available_deck,
                sorted_deck,
                prev_card,
                index
            )
    duplicate = []
    wildcards = [2, 7, 10]
    if available_deck != 'hidden' and\
    sorted_deck[index]["value"]\
    not in wildcards:
        duplicate =\
            get_playable_cards(
                sorted_deck,
                index
            )

    selected_card =\
        get_played_card(
            sorted_deck,
            index
        )

    if len(duplicate) > 1:
            played_card = duplicate
            for card in played_card:
                send_msg_to_user(
                    f'Opponent played: {card["name"]}'
                )
    else:
        played_card = selected_card
        send_msg_to_user(
            f'Opponent Played: {played_card["name"]}'
        )
    return played_card


def get_playable_cards(
    sorted_deck: list,
    index
) -> (list):
    '''
    checks if there are duplicates in deck and returns them
    '''
    end = index + 4
    grouped_cards = sorted_deck[index: end]
    duplicate = []
    for card in grouped_cards:
        if grouped_cards[0]["value"] == card['value']:
            duplicate.append(card)
    return duplicate

def generate_random_number(
    value_a: int,
    value_b: int
) -> (int):
    '''
    generates a random number in order to define AI behaviour
    returns int
    '''
    return random.randrange(value_a, value_b)


def select_choice_from_random(
    available_deck: str,
    random_number: int,
    playable_deck: list,
    prev_card: dict,
    enemy_is_winning: bool
) -> (int):
    '''
    returns selected index from random_number
    '''
    if random_number < 4:
        index = select_randomly(playable_deck)
    elif 4 <= random_number < 10:
        index =\
            select_an_ok_choice(
                available_deck,
                playable_deck,
                prev_card,
                enemy_is_winning
            )
    return index


def select_randomly(
    sorted_deck: list
) -> (int):
    '''
    select a random card from deck returns index
    '''
    return random.choice(range(len(sorted_deck)))


def select_an_ok_choice(
    available_deck: str,
    sorted_deck: list,
    prev_card: dict,
    enemy_is_winning: bool
) -> (int):
    '''
    let the AI select a decent play
    '''
    selected_index = None
    if enemy_is_winning and available_deck != 'hidden': # play high if enemy is winning
        sorted_deck.reverse()
        if not prev_card or\
        sorted_deck[0]['value'] >= prev_card['value']:
            selected_index = 0
    elif available_deck != 'hidden': # play safe, play lowest possible card
        wildcards = [2, 7, 10]
        for i, card in enumerate(sorted_deck):
            if not prev_card\
            or card['value'] >= prev_card['value'] and\
            card['value'] not in wildcards:
                selected_index = i
                break
    else: # if hidden
        selected_index = select_randomly(sorted_deck)
    if selected_index is None: # else play other wildcards if no higher card is found
        value_list =\
            [card['value'] for card in sorted_deck]
        if value_list.count(7) > 0:
            selected_index = value_list.index(7)
        elif value_list.count(10) > 0:
            selected_index = value_list.index(10)
        elif value_list.count(2) > 0:
            selected_index = value_list.index(2)
    return selected_index
