 ## IDIOT CARD GAME

##### ABOUT

This is a card game called Idiot, written in Python



Game Rules:

> "Each player is handed 9 cards. 6 are placed on the table 3 of them side up. These cards can only be played once the cards in their hand are exhausted. The other 3 are the hand of each player. Players must play a card, which must be  higher than the previous play, otherwise they must pick up the discard pile. The cards 2, 7, 10 are wildcards that can reset values, reverse the play and bomb the discard pile respectively. Multiple values can be played and bomb the deck if their are 4 in the discard. Players must pick up a card from the deck once they play a card down. Whoever finishes the game with no cards left to play wins"



#### Instructions

###### Arguments:

In source directory:

- start game: with `main.py --start *name*` 
- read leaderboard: `main.py --leaderboard`
- read rules: `main.py --rules



###### Pyinstaller build

1. install pyinstaller with `pip install --user pyinstaller`

2. in terminal: `echo "export PATH=$PATH:~/.local/bin" > ~/.bash-profile`

3. in src/ directory run:

    `chmod +x ./build.sh` and

   `./build.sh`

4. then in the dist/ directory run `idiot game --start NAME` or with the args listed above!

