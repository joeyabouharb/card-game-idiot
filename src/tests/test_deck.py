import sys, os
sys.path.insert(0, os.path.abspath('./'))


import json
from game.read_write import *
from game.deck import *

def test_load_deck_data():
    data = load_deck_data()

    with open('../docs/deck.json', 'r') as json_file:
        test_deck = json.load(json_file)

    assert test_deck['deck'] == data

def test_shuffle_deck():
    test_data = load_deck_data()
    original_data = test_data.copy()
    shuffle_deck(test_data)
    assert test_data != original_data

def test_hand_player_cards():
    test_data = load_deck_data()
    shuffle_deck(test_data)
    test_deck = get_cards_in_deck(test_data)
    test_player_one_hand = [card for card in hand_player_cards(test_deck)]
    test_player_two_hand = [card for card in hand_player_cards(test_deck)]

    count = 0
    assert len(test_player_one_hand) == 9
    assert len(test_player_two_hand) == 9
    for card in test_deck:
        count += 1
        assert card not in test_player_one_hand
        assert card not in test_player_two_hand
    assert count == 34

def test_get_next_card_in_deck():
    test_data = load_deck_data()
    shuffle_deck(test_data)
    test_deck = get_cards_in_deck(test_data)

    test_player_one_hand = [card for card in hand_player_cards(test_deck)]
    test_player_two_hand = [card for card in hand_player_cards(test_deck)]

    test_card = get_next_card_in_deck(test_deck)
    count = 0
    for card in test_deck:
        assert card is not test_deck
        count += 1
    assert count == 33


def test_split_hand():
    test_data = load_deck_data()
    shuffle_deck(test_data)
    test_deck = get_cards_in_deck(test_data)

    test_player_one_hand = [card for card in hand_player_cards(test_deck)]

    test_dict = split_hand(test_player_one_hand)
    assert len(test_dict['user_hand']) == 3
    assert len(test_dict['hidden']) == 3
    assert len(test_dict['visible']) == 3
