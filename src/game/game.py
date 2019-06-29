'''
handles general gameplay, interactions with user and opponent, etc.
'''
import types
from user import prompt_user_turn
from read_write import load_deck_data
from deck import hand_player_cards, get_cards_in_deck, split_hand
from opponent import prompt_opponent_turn
from actions import *


def game():
    '''
    main function that exucutes gameplay
    '''
    wildcards = [2, 7, 10]
    data_load = load_deck_data()
    deck_generator = get_cards_in_deck(data_load)
    user_deck = hand_player_cards(deck_generator)
    opponent_deck = hand_player_cards(deck_generator)
    user_deck = split_hand(user_deck)
    opponent_deck = split_hand(opponent_deck)
    discard = []
    played_card = {}

    while True:
        if not played_card or played_card["value"] not in wildcards:
            played_card = player_turn(True, discard, user_deck, prompt_user_turn, deck_generator)
        else:
            print('huh?')
            played_card = {}

        if not user_deck:
            # msg += get_win_msg()
            # end_game(True, msg)
            break
        played_card = {'value': 1}
        # if not played_card or played_card['value'] not in wildcards:
        #     played_card = player_turn(False, discard, opponent_deck,\
        #                             prompt_opponent_turn, deck_generator)
        #     print('gotcha')
        # else:
        #     played_card = {}

        # if not opponent_deck:
        #     # msg = get_loose_msg()
        #     # end_game(False, msg)
        #     break


def player_turn(is_human: bool, discard: list,\
    user_deck: dict, prompt: types.FunctionType, deck_generator: types.GeneratorType) -> (dict):
    '''
    takes in game variables and function call to any player
    and prompts them to pick an available card
    returns picked card -> dict
    '''
    prev_card = get_previous_play(discard)
    available_deck = get_available_play(user_deck)
    print(available_deck)
    cannot_play = check_user_can_play(user_deck[available_deck], prev_card)
    print(cannot_play)
    hand = user_deck['user_hand']
    if cannot_play:
        add_discard_to_hand(discard, user_deck)
        return False

    played_card = prompt(available_deck, user_deck, prev_card)
    new_card = get_next_card_in_deck(deck_generator)
    user_deck['user_hand'].append(new_card)
    wild_card_turn, is_wildcard =\
        check_for_wild_card(is_human, played_card, discard, user_deck)

    if is_wildcard:
        new_card = get_next_card_in_deck(deck_generator)
        user_deck['user_hand'].append(new_card)

    return wild_card_turn


game()
