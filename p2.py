#Ask the user for a number. Depending on whether the number is even 
#or odd, print out an appropriate message to the user.

try:
    num = int(raw_input('Enter a number \n'))
except:
    flag = 1
    while(flag):
        print 'Enter a valid number..'
        num = raw_input('Enter a number \n')
        if num.isdigit():
                break
        else:
            flag += 1


if int(num) % 2 ==0:
    print 'The number', num, ' is an even number'
else:
    print 'The number', num, ' is an odd number'

