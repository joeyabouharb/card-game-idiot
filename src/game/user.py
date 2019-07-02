'''
module to handle user turn
'''
from card_selector import validate_user_input,\
    get_played_card


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
    output = '\nNumber of cards in hand:\n'
    output += f'{opponent_stats["cards_in_hand"]}\n'
    output += 'opponents visible cards: \n'
    for card in opponent_stats['visible']:
        output += f'{card["name"]}\n'
    return f'{output}'

def prompt_user_turn(available_deck: str, user_deck: dict,\
    prev_card: dict, oppenent_stats: dict, wildcard={}) -> (dict):
    '''
    prompt user turn returns the selected card as dict
    '''

    deck = stringify_deck(user_deck, available_deck)
    wildcard_played = "" if not wildcard else f'{wildcard["name"]} - Wildcard Played!\n'
    previous = "\nNo cards in discard\n" if not prev_card\
        else f'\nBeat Previous Card {prev_card["name"]}\n'
    stats = display_opponent_stats(oppenent_stats)
    view =  f'{stats}\n{wildcard_played}\n{previous}\n{deck}\n'
    print(view)

    user_input = None
    index = None
    user_hand = user_deck[available_deck]

    while index is None:
        user_input = input('Select available options, or type pick to pick from pile: ')
        index = validate_user_input(available_deck, user_input, user_hand, prev_card)
    print(prev_card)
    print(user_hand[index])

    return get_played_card(user_hand, index)
