'''
read write functionality to read rules and leaderboards
'''
import json
from pathlib import Path

def read_from_game_rules():
    '''
    read rules from file
    '''
    with open('../docs/rules.txt') as file:
        read = file.read()
    return read

def read_from_leaderboard():
    filename = Path('../docs/leaderboard.json')

    if not filename.is_file():
        create_leaderboard(filename)

    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    leaderboard = data['leaderboard']
    return leaderboard if any(user['name'] for user in leaderboard)\
        else ''

def create_leaderboard(filename: Path):
    data = {
        'leaderboard': [
        ]
    }
    with open(filename, 'w+') as read_file:
        json.dump({data}, read_file, indent=2)

def stringify_leaderboard(leaderboard: list):
    output = 'Current Leaderboard: \n'
    for user in leaderboard:
        output += f'Name: {user["name"]}\nScore: {user["score"]}'
    return output
