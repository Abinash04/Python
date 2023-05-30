'''Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

import sys
a='yes'
def game():
    print "1. Rock\n"
    print "2. Scissors\n"
    print "3. Paper\n"
    ask1 = raw_input('Enter your choice : Player 1 \n')
    print 'Player 1 chose: ', ask1
    ask2 = raw_input('Enter your choice : Player 2 \n')
    print 'Player 2 chose: ', ask2
    
    if ask1 == 'Rock' and ask2 == 'Scissors':
        print "Congratulations !!! Player 1. You are the Winner! \n"
        again = raw_input('Player 1, Do you want to start a New game ? \n')
    elif ask1 == 'Scissors' and ask2 == 'Paper':
        print "Congratulations !!! Player 1. You are the Winner! \n"
        again = raw_input('Player 1, Do you want to start a New game ? \n')
    elif ask1 == 'Paper' and ask2 == 'Rock':
        print "Congratulations !!! Player 1. You are the Winner! \n"
        again = raw_input('Player 1, Do you want to start a New game ? \n')
    else:
        print "Congratulations !!! Player 2. You are the Winner! \n"
        again = raw_input('Player 2, Do you want to start a New game ? \n')
    if again == a:
        game()
    else:
        print 'exiting...'
        sys.exit()

game()






