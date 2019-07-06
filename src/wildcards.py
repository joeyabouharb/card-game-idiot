'''
handles wildcard plays
'''

import types
from actions import (
    get_previous_play, check_for_wild_card,
    get_reversed_value, check_user_can_play,
    add_discard_to_hand, add_to_discard,
)

def two_is_played(prompt: types.FunctionType, available_deck: str,\
    deck: dict, discard: list, opponent_stats: dict) -> (dict, bool):
    '''
    two is played
    '''
    played_card = get_previous_play(discard)
    played_card = prompt(
        available_deck, deck, played_card, opponent_stats
    )
    card = (
        played_card
        if isinstance(played_card, dict)
        else played_card[0]
    )
    is_wildcard = check_for_wild_card(card)
    return (
        played_card,
        is_wildcard
    )

def seven_is_played(prompt: types.FunctionType, available_deck: str,\
    deck: dict, discard: list, opponent_stats: dict) -> (dict, bool):
    '''
    when a seven is played
    '''
    played_card = get_previous_play(discard)
    card_to_match = get_reversed_value(discard)
    cannot_play = check_user_can_play(deck[available_deck], card_to_match)
    if cannot_play and available_deck != 'hidden':
        add_discard_to_hand(discard, deck['user_hand'])
        return {}, False
    played_card = prompt(
        available_deck, deck, card_to_match, opponent_stats, played_card\
    )
    card = (
        played_card
        if isinstance(played_card, dict)
        else played_card[0]
    )
    is_wildcard = check_for_wild_card(card)

    if available_deck == 'hidden':
        if not is_wildcard and card_to_match and\
        played_card['value'] < card_to_match['value']:
            add_to_discard(discard, played_card, deck)
            add_discard_to_hand(discard, deck['user_hand'])
            return {}, False
    return (
        played_card,
        is_wildcard
    )


def ten_is_played(prompt: types.FunctionType, available_deck: str,\
    deck: dict, discard: list, opponent_stats: dict) -> (dict, bool):
    '''
    ten is played
    '''
    discard.clear()
    played_card = prompt(available_deck, deck, {}, opponent_stats)
    card = (
        played_card
        if isinstance(played_card, dict)
        else played_card[0]
    )
    is_wildcard = check_for_wild_card(card)
    return (
        played_card,
        is_wildcard
    )
