'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python'''

import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
print 'List in a: ',a
for i in a:
    if i in b:
        try:
          c.append(i)
        except:
            pass

print set(c)
rnum = []
for k in range(1,10):
    rand_num = random.randint(1,99)
    rnum.append(rand_num)

print 'random list: ',rnum
print 'list in b: ',b
d = []
for i in rnum:
    if i in b:
        try:
            d.append(j)
        except:
            pass
print d

one=random.sample(range(1,100),25)
print one
two=random.sample(range(12,67),15)
print two
f = []
for m in one:
    if m in two:
      f.append(m)

print 'matched list:', f

g = [ item for item in a if (item in b)]
print 'List in G: ',set(g)
        
