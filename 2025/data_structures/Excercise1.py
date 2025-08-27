#############################################
# 20 tricky python data structures questions
#############################################

# 1. Lists
a = [1,2,3]
b = a # a and b reference the same object
b.append(4)
print(a)

# 2.
a = [[]] * 3
a[0].append(1)
print(a)
 # TODO: why not # [[1],[],[]]?

# 3.
a = [1,2,3,4,5]
print(a[::-1]) ## TODO: how does slicing works here

# 4.
a = [1,2,3]
print(a*3) # TODO: how come [1,2,3,1,2,3,1,2,3]

# 5. Tuples
a = (1,2,[3,4])
a[2].append(5) # TODO: tuples are immutable then why does this work.

# 6. 
a = (1)
b = (1,)
print(type(a), type(b))

# 7. Sets
a = {1,2,3}
b = {3,4,5}
print(a&b, a|b, a-b)

# 8.
# a = {1,2,3,[4,5]} #TODO: valid or not unhashable type list.

# 9.
a = {True, 1 , 2}
print(a) # TODO: why does True and 1 merge?

# 10. Dictionaries
a = {1: 'x', True: 'y'}
print(a)

# 11. 
a = {}
# a[[]] = "test" #TODO: error or not?
# print(a)

# 12.
a = {}
a[1] = "int"
a[1.0] = "float"
print(a)

# 13.
d = {"a": 1, "b": 2} 
for k in d: d[k] += 1  #TODO: is modifying values safe while looping?
print(d)

# 14.
from collections import defaultdict
d = defaultdict(int)
d['x'] += 1
print(d)


# 15. Strings
a = "hello"
print(a[::-1])

# 16.
a = "hello"
# a[0] = "H"
print(a)

# 17. 
print("".join(sorted("banana")))

# 18.
a = "abc"
b = "abc"
c = b
print(a is b)
print(a.index)
print(b.index)
print(c.index)

# 19.
x = [1,2,3]
y = (1,2,3)
print(x.__sizeof__(), y.__sizeof__())

# 20.
a = [1,2,3]
b = (i*i for i in a) # generator expression #TODO: how is it diff than list comprehension?
print(list(b))