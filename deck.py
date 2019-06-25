'''
handles deck shuffling and other actions...
'''

import types
import random


def shuffle_deck(deck: list)-> list:
    '''
    responsible for shuffling the deck at the start of the game
    returns list
    '''
    random.shuffle(deck)
    random.shuffle(deck)
    return deck


def get_cards_in_deck(deck: list)-> types.GeneratorType:
    '''
    handles the passing and giving of cards in existing deck
    returns items as generator
    '''
    for card in random.sample(deck, len(deck)):
        yield card


def hand_player_cards(deck: types.GeneratorType)-> list:
    '''
    hand each user 9 cards at the start of the game
    '''

    user_deck = []
    for _ in range(9):
        card = next(deck)
        user_deck.append(card)
    return user_deck


def get_next_card_in_deck(deck: types.GeneratorType)-> str:
    '''
    return next card in deck
    '''
    return next(deck)
