'''
handles general gameplay, interactions with user and opponent, etc.
'''
import types
from user import prompt_user_turn, send_msg_to_user
from actions import (
    add_discard_to_hand, add_to_discard,
    get_available_play, get_previous_play,
    check_user_can_play, check_for_wild_card,
    get_next_turn, end_game,
    stringify_result, check_if_game_ended,
    check_four_of_a_kind
)
from deck import (
    get_cards_in_deck, get_next_card_in_deck,
    split_hand, hand_player_cards
)

from read_write import (
    load_deck_data, load_leaderboard_data,
    save_game_results
)
from opponent import prompt_opponent_turn
from wildcards import (
    two_is_played, seven_is_played,
    ten_is_played
)


def game(name: str):
    '''
    main function that exucutes gameplay
    '''
    data_load = load_deck_data()
    deck_generator = get_cards_in_deck(data_load)
    user_deck = hand_player_cards(deck_generator)
    opponent_deck = hand_player_cards(deck_generator)
    user_deck = split_hand(user_deck)
    opponent_deck = split_hand(opponent_deck)

    discard = []
    played_card = {}
    is_human = False
    is_wildcard = False
    while not check_if_game_ended(user_deck, opponent_deck):
        (deck, opponent_stats, is_human)\
            = get_next_turn(is_human, user_deck, opponent_deck)
        (played_card, is_wildcard)\
            = player_turn(is_human, discard, deck, opponent_stats)
        (played_card)\
            = on_card_played(deck, played_card, deck_generator, discard)

        if played_card:
            if check_four_of_a_kind(discard) or\
            played_card['value'] == 10:
                is_wildcard = True
                is_bomb = True
            else:
                is_bomb = False

        while is_wildcard and\
            not check_if_game_ended(user_deck, opponent_deck):

            if not is_bomb:
                (deck, opponent_stats, is_human)\
                    = get_next_turn(is_human, user_deck, opponent_deck)

            (played_card, is_wildcard)\
                = prompt_wildcard_turn(is_human, discard, deck, opponent_stats, played_card)
            (played_card)\
                = on_card_played(deck, played_card, deck_generator, discard)

            if played_card:
                if check_four_of_a_kind(discard) or\
                played_card['value'] == 10:
                    is_wildcard = True
                    is_bomb = True
                else:
                    is_bomb = False



    result = end_game(user_deck, opponent_deck, is_human, name)
    send_msg_to_user(stringify_result(result))
    leaderboard = load_leaderboard_data()
    leaderboard_list = leaderboard
    save_game_results(leaderboard_list, result)


def on_card_played(deck: dict, played_card: dict,\
    deck_generator: types.GeneratorType, discard: dict):
    '''
    handles end of player turns
    '''
    if played_card:
        if isinstance(played_card, dict):
            add_to_discard(discard, played_card, deck)
        elif isinstance(played_card, list):
            for card in played_card:
                add_to_discard(discard, card, deck)
            played_card = played_card.pop()
        while len(deck['user_hand']) < 3:
            new_card = get_next_card_in_deck(deck_generator)
            if new_card:
                deck['user_hand'].append(new_card)
            else:
                break
    return played_card


def player_turn(is_human: bool, discard: list,\
    deck: dict, opponent_stats: dict) -> (dict, bool):
    '''
    takes in game variables and function call to any player
    and prompts them to pick an available card
    '''
    prev_card = get_previous_play(discard)
    available_deck = get_available_play(deck)
    cannot_play = check_user_can_play(deck[available_deck], prev_card)
    hand = deck['user_hand']

    if cannot_play and available_deck != 'hidden':
        add_discard_to_hand(discard, hand)
        player = 'You' if is_human else "Opponent"
        send_msg_to_user(f'{player} had no play! picked up discard :O')
        return {}, False

    prompt = prompt_user_turn if is_human else prompt_opponent_turn
    played_card = prompt(available_deck, deck, prev_card, opponent_stats)
    card = played_card if isinstance(played_card, dict) else played_card[0]
    is_wildcard = check_for_wild_card(card)

    if available_deck == 'hidden':
        if prev_card and not is_wildcard\
        and played_card['value'] < prev_card['value']:
            add_to_discard(discard, played_card, deck)
            add_discard_to_hand(discard, hand)
            user = 'You' if is_human else 'Opponent'
            send_msg_to_user(f'{user} had no play! picked up discard :(')
            return {}, False
    return played_card, is_wildcard


def prompt_wildcard_turn(is_human: bool, discard: list,\
    deck: dict, opponent_stats: dict, played_card: dict) -> (dict, bool):
    '''
    this prompt triggers when a wildcard is played and changes the state of the game
    '''
    available_deck = get_available_play(deck)
    prompt = prompt_user_turn if is_human else prompt_opponent_turn
    if played_card['value'] == 2:
        (card, is_wildcard)\
            = two_is_played(prompt, available_deck, deck, discard, opponent_stats)
    elif played_card['value'] == 7:
        (card, is_wildcard)\
            = seven_is_played(prompt, available_deck, deck, discard, opponent_stats)
    else:
        (card, is_wildcard)\
            = ten_is_played(prompt, available_deck, deck, discard, opponent_stats)
    return (
        card,
        is_wildcard
    )
