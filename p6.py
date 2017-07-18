#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

num = raw_input('Enter a string to find if its a PALINDROME ?\n')
print 'The string is:', num
rev = ''.join(reversed(num))

print 'Palindrome ',rev

'''Another way of finding reverse
rev1 = num [::-1]
print rev1'''

if num == rev1:
    print 'Palindrome'
else:
    print "Not a Palindrome"


