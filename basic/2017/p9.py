'''Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons from
the very first exercise)

Extras:

Keep the game going until the user types ¿exit¿
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

import random
b = 'yes'
a = random.randint(1,9)
print 'Random number ', a
guess = int(raw_input('Enter a guess between 1 to 9 \n'))
print 'your guessed number: ', guess
if guess == a:
    print 'you guessed exactly right \n'
elif guess > 1 and guess < 5:
    print 'you guessed too low \n'
else:
    print 'you guessed too high \n'

while b == 'yes':
    
