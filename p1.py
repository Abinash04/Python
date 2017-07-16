#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that 
#tells them the year that they will turn 100 years old.

import sys
name = raw_input('Please enter your name \n')
try:
    age = int(raw_input('Please enter your age \n'))
except:
    flag = 1
    while(flag):
        print 'Please enter age in numbers'
        age = raw_input('Please enter your age \n')
        if age.isdigit():
            break
        else:
            flag +=1
    
print 'Your name is', name, ' and your age is ', age
year = 2017
#print int(age)
#sys.exit()

if int(age) > 0 and int(age) < 100:
    h = 100 - int(age)
    year = 2017 + h
    print 'The year when you turn 100 years old is ', year
elif int(age) > 100:
    print ' Please enter age less than 100 '
else:
    print 'Please enter a valid age '


