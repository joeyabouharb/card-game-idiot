'''
handles general gameplay, interactions with user and opponent, etc.
'''
from .user import prompt_user_turn
from .actions import (
    add_discard_to_hand, add_to_discard,
    get_available_play, get_previous_play,
    check_user_can_play, check_for_wild_card,
    get_reversed_value
)
from .deck import (
    get_cards_in_deck, get_next_card_in_deck,
    split_hand, hand_player_cards
)
from .read_write import load_deck_data
from .opponent import prompt_opponent_turn


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

        played_card, is_wildcard =\
            player_turn(is_human, discard, deck, opponent_stats)

        if played_card:
            add_to_discard(discard, played_card, deck)

            if len(deck['user_hand']) < 3:
                new_card = get_next_card_in_deck(deck_generator)
                if new_card:
                    deck['user_hand'].append(new_card)

        while is_wildcard and\
            not check_if_game_ended(user_deck, opponent_deck):
            if played_card['value'] != 10:
                deck, opponent_stats, is_human\
                    = get_next_turn(is_human, user_deck, opponent_deck)
            played_card,\
            is_wildcard = prompt_wildcard_turn(is_human, played_card, discard, deck, opponent_stats)
            if played_card:
                add_to_discard(discard, played_card, deck)
                new_card = get_next_card_in_deck(deck_generator)
            if new_card:
                deck['user_hand'].append(new_card)


def check_if_game_ended(user_deck: dict, opponent_deck: dict) -> (bool):
    '''
    checks if cards have been exhausted from both player decks
    '''
    return (
        all(not filled for filled in user_deck.values()) or
        all(not filled for filled in opponent_deck.values())
    )


def end_game(deck: dict, is_human: bool):
    '''
    handles end game by saving the game score in file
    '''
    return 'not implemented'


def player_turn(is_human: bool, discard: list,\
    deck: dict, opponent_stats: dict) -> (dict):
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
        return {}, False

    prompt = prompt_user_turn if is_human else prompt_opponent_turn
    played_card = prompt(available_deck, deck, prev_card, opponent_stats)

    is_wildcard = check_for_wild_card(played_card)
    if available_deck == 'hidden':
        if not is_wildcard and not prev_card and\
        played_card['value'] < prev_card['value']:
            add_to_discard(discard, played_card, deck)
            add_discard_to_hand(discard, hand)
            return {}, False

    return played_card, is_wildcard


def prompt_wildcard_turn(is_human: bool, played_card: dict,\
    discard: list, deck: dict, opponent_stats: dict) -> (dict):
    '''
    this prompt triggers when a wildcard is played and changes the state of the game
    '''
    available_deck = get_available_play(deck)
    if played_card['value'] == 2:
        prompt = prompt_user_turn if is_human else prompt_opponent_turn
        played_card = prompt(available_deck, deck, played_card, opponent_stats, played_card)
        is_wildcard = check_for_wild_card(played_card)

    elif played_card['value'] == 7:
        prompt = prompt_user_turn if is_human else prompt_opponent_turn
        card_to_match = get_reversed_value(discard)
        cannot_play = check_user_can_play(deck[available_deck], card_to_match)
        if cannot_play and available_deck != 'hidden':
            add_discard_to_hand(discard, deck['user_hand'])
            return {}, False
        played_card = prompt(\
            available_deck, deck, card_to_match, opponent_stats, played_card\
        )
        is_wildcard = check_for_wild_card(played_card)
        if available_deck == 'hidden':
            if not is_wildcard and not card_to_match and\
                played_card['value'] < card_to_match['value']:
                add_to_discard(discard, played_card, deck)
                add_discard_to_hand(discard, deck['user_hand'])
                return {}, False

    elif played_card['value'] == 10:
        prompt = prompt_user_turn if is_human else prompt_opponent_turn
        discard.clear()
        played_card = prompt(available_deck, deck, {}, opponent_stats)
        is_wildcard = check_for_wild_card(played_card)

    return played_card,\
            is_wildcard


def get_next_turn(is_human: bool, user_deck: dict, opponent_deck: dict) -> (dict):
    '''
    get's the next turn in game
    '''
    is_human = not is_human
    deck = user_deck if is_human else opponent_deck
    opponent_deck = opponent_deck if is_human else user_deck
    opponent_stats = {
        "cards_in_hand": len(opponent_deck['user_hand']),
        "visible": opponent_deck['visible']
    }
    return deck, opponent_stats, is_human

if __name__ == '__main__':
    game('hello')
    