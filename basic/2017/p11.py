'''Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list
of only the first and last elements of the given list.
For practice, write this code inside a function.'''

import random
list1 = random.sample(range(1,30),8)

list2 = [ y for y in random.sample(range(1,30),8) if y[0] ]
print 'random list->',list1,'\ncomprehensive list',list2
