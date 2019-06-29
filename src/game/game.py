'''
handles general gameplay, interactions with user and opponent, etc.
'''
from user import prompt_user_turn
from wildcards import (
    ten_is_played, two_is_played,
    seven_is_played
)
from actions import (
    add_discard_to_hand, add_to_discard,
    get_available_play, get_previous_play,
    check_user_can_play, check_for_wild_card
)
from deck import (
    get_cards_in_deck, get_next_card_in_deck,
    split_hand, hand_player_cards
)
from read_write import load_deck_data
from opponent import prompt_opponent_turn

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

    discard = []
    played_card = {}
    is_human = False
    is_wildcard = False

    while True:
        if not is_wildcard:
            # deck = user_deck if is_human else opponent_deck
            deck = user_deck
            is_human = True
            played_card, is_wildcard =\
                player_turn(is_human, discard, deck)
            if played_card:
                add_to_discard(discard, played_card, deck)

                if len(deck['user_hand']) < 3:
                    new_card = get_next_card_in_deck(deck_generator)
                    deck['user_hand'].append(new_card)

        while is_wildcard:
            # deck = user_deck if is_human else opponent_deck
            deck = user_deck
            played_card, is_wildcard =\
                prompt_wildcard_turn(is_human, played_card, discard, deck, opponent_deck)

            add_to_discard(discard, played_card, deck)
            new_card = get_next_card_in_deck(deck_generator)
            deck['user_hand'].append(new_card)

        if not user_deck:
            # msg += get_win_msg()
            # end_game(True, msg)
            break


def player_turn(is_human: bool, discard: list, deck: dict) -> (dict):
    '''
    takes in game variables and function call to any player
    and prompts them to pick an available card
    -- is_human: bool handles turns between user and AI
    --discard: discard pile list
    --deck: current player deck
    returns picked card -> dict
    '''

    prev_card = get_previous_play(discard)
    available_deck = get_available_play(deck)
    cannot_play = check_user_can_play(deck[available_deck], prev_card)
    hand = deck['user_hand']

    if cannot_play:
        add_discard_to_hand(discard, hand)
        return {}, False

    prompt = prompt_user_turn if is_human else prompt_opponent_turn
    played_card = prompt(available_deck, deck, prev_card)
    is_wildcard = check_for_wild_card(played_card)

    return played_card, is_wildcard


def prompt_wildcard_turn(is_human: bool, played_card: dict,\
    discard: list, user_deck: dict, enemy_deck: dict) -> (dict):
    '''
    this prompt triggers when a wildcard is played and changes the state of the game
    --is_human: determines if it is an AI Turn - bool
    --played_card: wildcard that was played - dict
    -- discard: discard pile - list
    -- user_deck dict - list
    -- enemy_deck enemy's deck - dict
    returns -> dict new card played
    '''
    available_deck = get_available_play(user_deck)

    if played_card['value'] == 2:
        # prompt = prompt_opponent_turn if is_human else prompt_user_turn
        prompt = prompt_user_turn
        # deck = enemy_deck if is_human else user_deck
        deck = user_deck
        played_card = two_is_played(prompt, played_card, deck, available_deck)
        is_wildcard = check_for_wild_card(played_card)
    elif played_card['value'] == 7:
        # prompt = prompt_opponent_turn if is_human else prompt_user_turn
        prompt = prompt_user_turn
        card_to_match = discard[1]
        # deck = enemy_deck if is_human else user_deck
        deck = user_deck
        played_card = seven_is_played(\
            prompt, played_card, deck, available_deck, card_to_match\
        )
        is_wildcard = check_for_wild_card(played_card)
    elif played_card['value'] == 10:
        # deck = user_deck if is_human else enemy_deck
        deck = user_deck
        # prompt = prompt_user_turn if is_human else prompt_opponent_turn
        discard.clear()
        prompt = prompt_user_turn
        played_card = ten_is_played(prompt, deck, available_deck, played_card)
        is_wildcard = check_for_wild_card(played_card)

    return played_card, is_wildcard


game()
