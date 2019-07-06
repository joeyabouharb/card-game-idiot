#! /bin/bash


echo 'buidling idiot...';
source ~/.bash-profile;
pyinstaller main.py --onefile --clean --name idiotgame;
rm -rf build/
exit 2

