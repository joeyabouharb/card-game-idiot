'''
handle wildcard usage
'''
import types


def two_is_played(prompt: types.FunctionType, wild_card: dict,\
    deck: dict, available_deck: dict) -> (dict):
    '''
    calls the prompt function to the appropriate player and handles wildcard
    '''
    return prompt(available_deck, deck, wild_card, wild_card)


def seven_is_played(prompt: types.FunctionType, wildcard: dict,\
    deck: dict, available_deck: dict, prev_card: dict) -> (dict):
    '''
    calls the prompt function to the appropriate player and handles wildcard
    '''
    return prompt(available_deck, deck, prev_card, wildcard)


def ten_is_played(prompt: types.FunctionType, deck: dict,\
    available_deck: str, wild_card: dict) -> (dict):
    '''
    calls the prompt function to the appropriate player and handles wildcard
    '''
    return prompt(available_deck, deck, {"value": 0}, wild_card)
