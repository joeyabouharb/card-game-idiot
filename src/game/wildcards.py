'''
handle wildcard usage
'''
from user import prompt_user_turn
from opponent import prompt_opponent_turn


def two_is_played(is_human: bool, wild_card: dict,\
    user_deck: dict, available_deck: str, prev_card: dict):

    if is_human:
        prompt_opponent_turn(available_deck, user_deck, wild_card)

    return prompt_user_turn(available_deck, user_deck, prev_card, wild_card)


def seven_is_played(is_human: bool, wild_card: dict,\
    user_deck: dict, available_deck: str, prev_card: dict):
    if is_human:
        prompt_opponent_turn(available_deck, user_deck, wild_card)

    return prompt_user_turn(available_deck, user_deck, prev_card, wild_card)


def ten_is_played(is_human: bool, user_deck: dict,\
    available_deck: str, wild_card: dict, prev_card: dict):

    if is_human:
        if not user_deck:
            pass
            # msg = get_win_msg()
            # end_game(msg)
        else:
            
            return prompt_user_turn(available_deck, user_deck, prev_card, wild_card)
    else:
        if not user_deck:
            pass
            # msg = get_looser_msg()
            # end_game(msg)
        return prompt_opponent_turn(available_deck, user_deck, wild_card)
