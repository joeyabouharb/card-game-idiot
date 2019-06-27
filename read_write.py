'''
Handles read and write to file system, loading and saving game data.
'''


import json

def load_deck_data()-> (list):
    '''
    loads data from deck.json file and returns the deck as a list
    '''

    with open('deck.json', 'r') as json_file:
        data = json.load(json_file)
    return data['deck']