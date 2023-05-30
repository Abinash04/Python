#!/usr/bin/python3

'''6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output : 
    List : ['3', ' 5', ' 7', ' 23'] 
    Tuple : ('3', ' 5', ' 7', ' 23')
'''

print("welcome to python3")
num = input("Enter comma separated numbers: ")

d = num.split(',')

b = tuple(d)
print("List: "+str(d)+ "\nTuple: "+str(b))
