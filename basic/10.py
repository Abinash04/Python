#!/usr/bin/python3

'''10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5 
Expected Result : 615'''

num = int(input("Enter a number: "))
#print("Expected Result : "+str(num+num*num+num*num*num))
n1 = int("%s" % num )
print(n1)
n2 = int("%s%s" % (num,num))
n3 = int("%s%s%s" %(num,num,num))
print(n1+n2+n3)

