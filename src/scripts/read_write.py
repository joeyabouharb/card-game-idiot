'''
read write functionality to read rules and leaderboards
'''

def read_from_game_rules():
    '''
    read rules from file
    '''
    with open('../docs/rules.txt') as file:
        read = file.read()
    return read