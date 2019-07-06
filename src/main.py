#!/bin/python
'''
Program: Idiot game App
Author: Joseph Abouharb
email: ****
github: joeyabouharb
Licence: MIT Liscence

Have Fun!
'''
import argparse
from game import game
from read_data import (
    read_from_game_rules, read_from_leaderboard,
    stringify_leaderboard
)


def main():
    '''
    main app
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--rules', help='shows game rules', action='store_true')
    parser.add_argument('--start', '-s', help='start a game with player name', dest='name')
    parser.add_argument('--leaderboard', help='read leaderboard', action='store_true')
    args = parser.parse_args()
    if args.name:
        name = args.name
        game(name)
    elif args.rules:
        print(read_from_game_rules())
    elif args.leaderboard:
        leaderboard = read_from_leaderboard()
        if not leaderboard:
            msg = 'nothing found'
        else:
            msg = stringify_leaderboard(leaderboard)
        print(msg)
if __name__ == '__main__':
    main()
