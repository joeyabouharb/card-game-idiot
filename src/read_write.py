'''
module to handle read and write to file system -
loading and saving game data.
'''
import json


def load_deck_data() -> (list):
    '''
    loads data from deck.json file and returns the deck as a list
    '''
    with open('../docs/deck.json', 'r') as json_file:
        data = json.load(json_file)
    return data['deck']


def load_leaderboard_data() -> (list):
    '''
    loads leaderboard data
    '''
    with open('../docs/leaderboard.json', 'r') as leaderboard:
        data = json.load(leaderboard)
    return data['leaderboard']


def save_game_results(leaderboard: list, score: dict):
    '''
    saves game score into file
    '''
    leaderboard.append(score)
    with open('../docs/leaderboard.json', 'w+') as json_file:
        json.dump({
            "leaderboard": leaderboard
        }, json_file, indent=2)
