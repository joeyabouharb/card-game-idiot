'''
handles deck shuffling and other actions...
'''

import types
import random


def shuffle_deck(deck: list)-> (list):
    '''
    responsible for shuffling the deck at the start of the game
    returns list
    '''
    random.shuffle(deck)
    random.shuffle(deck)
    return deck


def get_cards_in_deck(deck: list)-> (types.GeneratorType):
    '''
    handles the passing and giving of cards in existing deck
    returns items as generator
    '''
    for card in random.sample(deck, len(deck)):
        yield card


def hand_player_cards(deck: types.GeneratorType)-> (list):
    '''
    hand each user 9 cards at the start of the game
    '''

    user_deck = []
    for _ in range(9):
        card = next(deck)
        user_deck.append(card)
    return user_deck


def split_hand(hand: list) -> (dict):
    '''
    takes the hand and splits them into dictionary
    -user_hand
    -visible
    -hidden
    '''
    user_hand= [hand.pop(n) for n in random.sample(range(len(hand)-2), 3)]
    visible = [hand.pop(n) for n in random.sample(range(len(hand)-2), 3)]
    hidden = hand

    user_cards = {
        "user_hand": user_hand,
        "visible": visible,
        "hidden": hidden
    }

    return user_cards


def get_next_card_in_deck(deck: types.GeneratorType)-> (dict):
    '''
    return next card in deck
    '''
    return next(deck)


def check_if_deck_empty(next_out, deck: types.GeneratorType) -> (bool):
    '''
    check if generator is exausted
    '''
    if next_out is None:
        return False
    return True