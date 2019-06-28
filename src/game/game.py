'''
handles general gameplay, interactions with user and opponent, etc.
'''


import types
from read_write import load_deck_data
from deck import hand_player_cards, get_cards_in_deck, split_hand
from user import prompt_user_turn
from opponent import prompt_opponent_turn
from actions import add_to_discard,\
    check_user_can_play,\
    get_previous_play,\
    add_discard_to_hand,\
    reset_wildcard_values


def game():
    '''
    main function that exucutes gameplay
    '''
    data_load = load_deck_data()
    deck_generator = get_cards_in_deck(data_load)
    user_deck = hand_player_cards(deck_generator)
    opponent_deck = hand_player_cards(deck_generator)
    user_deck = split_hand(user_deck)
    opponent_deck = split_hand(opponent_deck)
    AI_possible_wildcard = dict()
    user_possible_wildcard = dict()

    while user_deck is not False\
        or opponent_deck is not False:
        discard = []

        prev_card = get_previous_play(discard)
        available_deck = get_available_play(user_deck)
        can_user_play = check_user_can_play(available_deck, prev_card)

        opp_available_deck = get_available_play(opponent_deck)
        prev_card = get_previous_play(discard)
        can_opp_play = check_user_can_play(opp_available_deck, prev_card)

    if not user_deck:
        msg = 'you win'
    else: 
        msg = 'you loose!'
    print(msg)


def get_available_play(user_deck: dict) ->(dict):
    '''
    checks what current deck the user could play returns the single dictionary item
    '''
    if user_deck['player_hand'] is not False:
        return { 'available': user_deck['player_hand'] }
    if user_deck['visible'] is not False:
        return { 'visible': user_deck['visible'] }
    return { 'hidden': user_deck['hidden'] }


def player_turn(can_user_play: bool, discard: list,\
    available_deck: list, prompt: types.FunctionType) -> (dict):

    if not can_user_play:
        add_discard_to_hand(discard, available_deck)
    else:
        user_play = prompt(available_deck, discard)
        add_to_discard(discard, user_play)
