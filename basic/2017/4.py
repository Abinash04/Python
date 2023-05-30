#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import sys
import re
import os
#sys.setrecursionlimit(2000)
import time
thefile = os.path.join(os.path.dirname(__file__), '4.py_output.txt')
start = time.time()


def reverse(j):
        rev = 0
        while j > 0:
                rem = j % 10
                rev = (rev * 10) + rem
                j = j // 10
        return rev
		
num=999
def recursive(num):
        for c in list(reversed(range(100,1000))):
                last=list(reversed(range(100,1000)))[-1]
                k=num * c
                a=reverse(k)
                
                if c == last:
                        recursive(num-1)
						
                if a == k:
                        if len(str(a))== 6 and re.match('^9',str(a)):
                                print "found",a
                                fo = open (thefile,'w')
                                fo.write("The largest palindrome made from the product of two 3-digit numbers:")
                                print>>fo,a
                                fo.close()
                                break
                                  
recursive(num)
end = time.time()
print(end - start)
    
