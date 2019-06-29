'''
helps validate player card selection and return the appropriate card
'''


def validate_user_input(user_input: str, user_deck: list,
                        prev_card: dict)-> (int):
    '''
    validates user input to int,
    checks if played card is higher than the prev_card and
    returns the integer as the index of the user deck
    '''

    user_input = user_input.strip()
    if not user_input.isdigit():
        return None
        # val = validate_user_input(
            # input('not a number try again: ', user_deck, prev_card))
    try:
        val = int(user_input) - 1
    except ValueError:
        return None
        # val = validate_user_input(input('please enter a number from 1-3... '))

    if val >= len(user_deck):
        return None
        # val = validate_user_input(
        #    input('please enter a number from 1-3 '), user_deck, prev_card)
    if not check_card_values(user_deck, prev_card, val):
        return None
        # val = validate_user_input(
        #    input('please enter a number from 1-3 '), user_deck, prev_card)

    return val


def check_card_values(user_deck: list, prev_card: dict, val: int)-> (bool):
    '''
    checks the player deck against the previous play,
    if no higher card is found return True or False
    '''
    if user_deck[val]['value'] == 2 or\
        user_deck[val]['value'] == 7 or\
        user_deck[val]['value'] == 10:
        return True

    if prev_card['value'] == 2 or\
        prev_card['value'] == 10:
            return True
    print(user_deck[val])
    print(prev_card)
    if user_deck[val]['value'] < prev_card['value']:
        return False
    return True



def get_played_card(user_deck: list, play_card: int)-> (dict):
    '''
    takes in the current user deck as list,
    and the play card which is int
    return's the item dictionary from the user_deck
    '''
    card = user_deck[play_card]
    return card

