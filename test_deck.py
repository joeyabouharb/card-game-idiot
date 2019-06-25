import json
from read_write import load_deck_data
from deck import shuffle_deck, hand_player_cards, get_cards_in_deck, get_next_card_in_deck

def test_load_deck_data():
    data = load_deck_data()

    with open('deck.json', 'r') as json_file:
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

