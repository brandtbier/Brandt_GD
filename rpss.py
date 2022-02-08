#Brandt Bier
#Rock Paper Scissors

import random
import os
os.system('clr')

def play():
    print('+-----------------------+')
    print("| Rock, Paper, Scissors |")
    print('|  [R] =   Rock         |')
    print('|  [P] =   Paper        |')
    print('|  [S] =   Scissors     |')
    print('+-----------------------+')
    user = input('Enter Your Descision-')
    user = user.lower()
    
    computer = random.choice(['r','p','s'])

    if user == computer:
        return ('Good game, it is a tie').format()
    if is_win(user, computer):
        return ('Good game, you won').format(user, computer)
    return ('Good game, but you lost, try again later')

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

if __name__ == '__main__':

    print(play())