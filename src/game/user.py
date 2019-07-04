'''
module to handle user turn
'''
import os
from game.card_selector import validate_user_input,\
    get_played_card


def send_msg_to_user(msg: str):
    '''
    prints a mesage to the user
    '''
    print(msg)


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


def display_opponent_stats(opponent_stats: dict):
    output = (
        '\nNumber of cards in hand:\n'
        f'{opponent_stats["cards_in_hand"]}\n'
        'opponents visible cards: \n'
    )

    for card in opponent_stats['visible']:
        output += f'{card["name"]}\n'
    return f'{output}'

def prompt_user_turn(available_deck: str, user_deck: dict,\
    prev_card: dict, oppenent_stats: dict, wildcard={}) -> (dict):
    '''
    prompt user turn returns the selected card as dict
    '''
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
    send_msg_to_user(view)

    user_input = None
    index = None
    user_hand = user_deck[available_deck]

    while index is None:
        user_input = input('\033[1A\033[KSelect available options, or type pick to pick up discard: ')
        index = validate_user_input(available_deck, user_input, user_hand, prev_card)

    return get_played_card(user_hand, index)
