# Tests should be run on the projects root directory in order for it to work
import sys, os
sys.path.insert(0, os.path.abspath('./'))

from game.actions import *
from game.card_selector import *
from game.deck import *
from game.read_write import load_deck_data


def test_validate_user_input():
    
    user_deck = [
        {"name": "10 of Clubs", "value": 10},
        {"name": "3 of Diamonds", "value":  3},
        {"name": "4 of Spades" , "value":  4},
        {"name": "2 of Diamonds", "value": 2}
    ]

    prev_card = {"name": "4 of Diamonds", "value":  4}

    assert validate_user_input('','1', user_deck, prev_card) == 0
    assert validate_user_input('', '2', user_deck, prev_card) is None
    assert validate_user_input('','3', user_deck, prev_card) == 2
    assert validate_user_input('', '5', user_deck, prev_card) is None
    assert validate_user_input('', 'd', user_deck, prev_card) is None
    assert validate_user_input('', '4', user_deck, prev_card) == 3
    assert not validate_user_input('', '423423 ', user_deck, prev_card)
def test_get_played_cards():
    user_deck = [
        {"name": "10 of Clubs", "value": 10},
        {"name": "3 of Diamonds", "value":  3},
        {"name": "4 of Spades" , "value":  4},
        {"name": "2 of Diamonds", "value": 2}
    ]

    prev_card = {"name": "4 of Diamonds", "value":  4}
    val = validate_user_input('test', '3', user_deck, prev_card)
    assert val == 2

    test_card = get_played_card(user_deck, val)
    assert test_card == user_deck[val]

def test_retrieve_previous_card():
    test_data = load_deck_data()
    shuffle_deck(test_data)
    test_deck = get_cards_in_deck(test_data)

    discard = []
    player_hand = {"user_hand": []}
    for _ in range(10):
        random_card = get_next_card_in_deck(test_deck)
        player_hand["user_hand"].append(random_card)
        add_to_discard(discard, random_card, player_hand)

    get_prev = get_previous_play(discard)
    assert get_prev == random_card

def test_check_for_wildcard():
    user_deck = [
        {"name": "10 of Clubs", "value": 10},
        {"name": "7 of Diamonds", "value":  7},
        {"name": "2 of Spades" , "value":  2},
        {"name": "8 of Spades" , "value":  8}
    ]

    prev_card = {"name": "4 of Diamonds", "value":  4}

    val = validate_user_input('', '2', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    assert test_card == user_deck[val]
    discard = [{"name": "4 of Diamonds", "value":  4}]
    test_wildcard = check_for_wild_card(test_card)

    assert test_wildcard is True

    val = validate_user_input('', '3', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    test_wildcard = check_for_wild_card(test_card)
    assert test_wildcard is True

    val = validate_user_input('', '1', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    test_wildcard = check_for_wild_card(test_card)
    assert test_wildcard is True

    val = validate_user_input('', '4', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    test_wildcard = check_for_wild_card(test_card)
    assert  test_wildcard is False

def test_four_of_a_kind():
    discard = [
                {"name": "8 of Clubs" , "value":  8},
                {"name": "8 of Spades" , "value":  8},
                {"name": "8 of Diamonds" , "value":  8},
                {"name": "2 of Clubs" , "value":  2}
    ]
    player_hand_test = {
        "user_hand": [
        {"name": "8 of Hearts" , "value":  8},
        {"name": "9 of Hearts" , "value":  9}
        ]
    }
    test_card = {"name": "8 of Hearts" , "value":  8}
    add_to_discard(discard, test_card, player_hand_test)
    check_four_of_a_kind(discard)
    assert not discard