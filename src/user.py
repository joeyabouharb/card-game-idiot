'''
module to handle user turn
'''
import os

from operator import (
    itemgetter
)
from card_selector import (
    validate_user_input,
    get_played_card,
    validate_multi_input
)

def send_msg_to_user(msg: str, prompt=True):
    '''
    prints a mesage to the user
    '''
    print(msg)
    if prompt:
        input('Enter to continue...')

def clear_output():
    '''
    clears out user prompt
    '''
    os.system('cls ' if os.name == 'nt' else 'clear')


def stringify_deck(user_deck: dict, available_deck: str) -> (str):
    '''
    grabs user's current available hand and  ->
    returns string
    '''
    msg = "user's current Hand:\n"
    for i, card in enumerate(user_deck[available_deck]):
        i += 1
        if available_deck == 'hidden':
            msg += f'{i}) #\t\t'
        else:
            msg += f'{i}) {card["name"]}\t\t'

    if user_deck['visible'] and available_deck != 'visible':
        msg += f'\nvisible on table: \n'
        for card in user_deck['visible']:
            msg += f'{card["name"]}\t'

    if user_deck['hidden'] and available_deck != 'hidden':
        msg += "\n"
        for card in user_deck['hidden']:
            msg += f'#\t\t'

    return msg


def display_opponent_stats(opponent_stats: dict) -> (str):
    '''
    displays available information about opponent
    '''
    output = (
        '\nNumber of cards in hand:\n'
        f'{opponent_stats["cards_in_hand"]}\n'
        'opponents visible cards: \n'
    )

    for card in opponent_stats['visible']:
        output += f'{card["name"]}\n'
    return f'{output}'


def sort_deck(available_deck: str, user_deck: dict):
    '''
    sorts the deck in order
    '''
    if available_deck == 'user_hand':
        sorted_deck = sorted(
            user_deck[available_deck],
            key=itemgetter('value')
        )
        user_deck[available_deck] = sorted_deck


def prompt_user_turn(available_deck: str, user_deck: dict,\
    prev_card: dict, oppenent_stats: dict, wildcard=False) -> (object):
    '''
    main prompt to display information to player and handle user play
    returns played card
    '''
    sort_deck(available_deck, user_deck)

    deck = stringify_deck(user_deck, available_deck)
    wildcard_played = (
        ""
        if not wildcard
        else
        f'{wildcard["name"]} - Wildcard Played!\n'
    )
    previous = (
        "\nNo cards in discard\n"
        if not prev_card
        else
        f'\nBeat Previous Card {prev_card["name"]}\n'
    )
    stats = display_opponent_stats(oppenent_stats)
    view = (
        f'{stats}\n'
        f'{wildcard_played}\n'
        f'{previous}\n' + f'{deck}\n'
    )
    send_msg_to_user(view, False)
    play = handle_user_play(available_deck, user_deck, prev_card)
    if available_deck == 'hidden':
        send_msg_to_user(f'played: {play["name"]}')
    clear_output()
    return play


def handle_user_play(\
    available_deck: str, user_deck: dict,\
    prev_card: dict) -> (object):
    '''
    function that handles user input, determines whether
    user is playing multiple cards or not
    '''
    user_hand = user_deck[available_deck]
    play = {}
    while not play:
        user_input = input('\033[1A\033[KSelect available options: ')
        split_input = user_input.split(' ')
        is_multiple = len(split_input) > 1
        if not is_multiple:
            index = validate_user_input(
                available_deck,
                user_input,
                user_hand,
                prev_card
            )
            if index is not None:
                play = get_played_card(
                    user_hand,
                    index
                )
        else:
            indexes = validate_multi_input(
                available_deck,
                split_input,
                user_hand,
                prev_card
            )
            play = []
            if indexes:
                for number in indexes:
                    play.append(
                        get_played_card(
                            user_hand,
                            number
                        )
                    )
    return play
