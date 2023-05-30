import random
min=1
max=6
roll='yes'


if (roll == "yes") or (roll == "y"):
        print 'Rolling the Dice ...'
        value = random.randint(min,max)
        print value
        if value == '6':
                print 'Wow!!! Rolling Again ...'
                val = random.randint(min,max)
                print val

roll = input('Do you want to roll the dice ?\n')
