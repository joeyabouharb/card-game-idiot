'''
module handling deck shuffling and dealing
'''
import types
import random


def shuffle_deck(
    deck: tuple
)-> (list):
    '''
    responsible for shuffling the deck at the start of the game
    returns list
    '''
    random.shuffle(deck)

    return deck


def get_cards_in_deck(
    deck: tuple
)-> (types.GeneratorType):

    for card in random.sample(deck, len(deck)):
        yield card


def hand_player_cards(
    deck: types.GeneratorType
)-> (list):
    '''
    hand each user 9 cards at the start of the game
    '''

    user_deck = []
    for _ in range(9):
        card = next(deck)
        user_deck.append(card)
    return user_deck


def split_hand(
    hand: list
) -> (dict):
    '''
    takes the hand and splits them into dictionary
    -user_hand
    -visible
    -hidden
    '''
    user_hand = [
        hand.pop()
        for _ in range(3)
    ]
    visible = [
        hand.pop()
        for _ in range(3)
    ]
    hidden = hand

    return {
        "user_hand": user_hand,
        "visible": visible,
        "hidden": hidden
    }



def get_next_card_in_deck(
    deck: types.GeneratorType
)-> (dict):
    '''
    return next card in deck
    '''
    return next(deck, False)
