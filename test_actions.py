from actions import *
from deck import *
from read_write import load_deck_data


def test_validate_user_input():
    

    user_deck = [
        {"name": "10 of Clubs", "value": 10},
        {"name": "3 of Diamonds", "value":  3},
        {"name": "4 of Spades" , "value":  4},
        {"name": "2 of Diamonds", "value": 2}
    ]

    prev_card = {"name": "4 of Diamonds", "value":  4}

    assert validate_user_input('1', user_deck, prev_card) == 0
    assert validate_user_input('2', user_deck, prev_card) is None
    assert validate_user_input('3', user_deck, prev_card) == 2
    assert validate_user_input('5', user_deck, prev_card) is None
    assert validate_user_input('d', user_deck, prev_card) is None
    assert validate_user_input('4', user_deck, prev_card) == 3

def test_get_played_cards():
    user_deck = [
        {"name": "10 of Clubs", "value": 10},
        {"name": "3 of Diamonds", "value":  3},
        {"name": "4 of Spades" , "value":  4},
        {"name": "2 of Diamonds", "value": 2}
    ]
    prev_card = {"name": "4 of Diamonds", "value":  4}
    val = validate_user_input('3', user_deck, prev_card)
    assert val == 2

    test_card = get_played_card(user_deck, val)
    assert test_card == user_deck[val]

def test_retrieve_previous_card():
    test_data = load_deck_data()
    shuffle_deck(test_data)
    test_deck = get_cards_in_deck(test_data)

    discard = []
    for _ in range(10):
        random_card = get_next_card_in_deck(test_deck)
        add_to_discard(discard, random_card)

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

    val = validate_user_input('2', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    assert test_card == user_deck[val]
    discard = [{"name": "4 of Diamonds", "value":  4}]
    test_wildcard = check_for_wild_card(True, prev_card, test_card, discard )

    assert test_wildcard['value'] == prev_card['value']

    val = validate_user_input('3', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    test_wildcard = check_for_wild_card(True, prev_card, test_card, discard )
    assert test_wildcard['value'] == 0

    val = validate_user_input('1', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    test_wildcard = check_for_wild_card(True, prev_card, test_card, discard )
    assert test_wildcard is None
    assert not discard

    val = validate_user_input('4', user_deck, prev_card)
    test_card = get_played_card(user_deck, val)
    test_wildcard = check_for_wild_card(True, prev_card, test_card, discard )
    assert test_card is test_wildcard