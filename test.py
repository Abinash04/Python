import sys
import re
sys.setrecursionlimit(2000)
import time
start = time.time()


def reverse(j):
        rev = 0
        while j > 0:
                rem = j % 10
                rev = (rev * 10) + rem
                j = j // 10
        return rev
num=999
palindrome=[]
def recursive(num):
        for c in list(reversed(range(100,1000))):
                last=list(reversed(range(100,1000)))[-1]
                k=num * c
                a=reverse(k)
                
                if c == last:
                        #print num
                        #print last
                        recursive(num-1)
                if a == k:
                        if len(str(a))== 6 and re.match('^9',str(a)):
                                print "found",a
                                thefile = open('test.txt', 'w')
                                print>>thefile,a
                                break
                                #palindrome.append(a)
                        
                        
recursive(num)
#print palindrome
end = time.time()
print(end - start)
    
