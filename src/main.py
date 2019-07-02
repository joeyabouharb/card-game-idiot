'''
Program: Idiot game App
Author: Joseph Abouharb
email: joey.abouharb@gmail.com
github: joeyabouharb
Licence: MIT Liscence

Have Fun!
'''
import argparse
from game.game import game
from scripts.read_write import read_from_game_rules

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rules', help='shows game rules', action='store_true')
    parser.add_argument('--start', '-s', help='start a game with player name', dest='name')
    parser.add_argument('--leaderboard', help='read leaderboard')
    args = parser.parse_args()
    if args.name:
        name = args.name
        game(name)
    elif args.rules:
        print(read_from_game_rules())
    elif args.leaderboard:
        pass

if __name__ == '__main__':
    main()
