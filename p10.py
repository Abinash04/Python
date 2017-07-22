'''Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes. 
using at least one list comprehension'''

import collections
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list1 = random.sample(range(1,20),10)
print 'a->',a,'\nb->',b,'\nlist1->',list1

c = [ x for x in collections.Counter(a) for y in b if x==y]
print c
final = [ x for x in collections.Counter(list1) for y in b if x==y]
print 'final',final
