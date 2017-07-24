#Python Regular Expressions
'''Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') ? 'not candy'
not_string('x') ? 'not x'
not_string('not bad') ? 'not bad'''

import re
import random

def not_string(str):
  if re.match('^not',str):
    return str
  else:
    return 'not '+ str

k=not_string('abi')
#print k

def without_regexp(str):
  if str.startswith('not',0,3):
    return str
  else:
    return 'not '+ str

j = without_regexp('abiih')
#print j

def missing_char(str, n):
  return ''.join(str[i] for i in range(0,len(str)) if i!=n)

#print missing_char('abinash',4)

#Given a string, return a new string where the first and last chars have
#been exchanged.
def front_back(str):
 mid = str[1:-1]
 # last + mid + first
 return str[-1] + mid + str[0]
#print front_back('a')

#Given a string, we'll say that the front is the first 3 chars of the string.
#If the string length is less than 3, the
#front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
  while len(str) <=3:
    return str*3
  front = str[0:3]
  while len(str) >= 4:
    return front*3
#print front3('Java')

#Given a string and a non-negative int n, return a larger string that is n
#  copies of the original string.

def string_times(str, n):
  return str*n
#print string_times('abi',6)

#Given a string and a non-negative int n, we'll say that the front of the
#string is the first 3 chars, or whatever is there if the string is less than
#length 3. Return n copies of the front;

def front_times(str, n):
  while len(str) <=3:
    return str*n
  front = str[0:3]
  while len(str) >= 4:
    return front*n
#print front_times('Chocoloate',2)

#Given a string, return a new string made of every other char starting
#with the first, so "Hello" yields "Hlo".

def string_bits(str):
  return ''.join(str[i] for i in range(0,len(str)) if i%2==0)

print string_bits('Heeololeo')
  






























