#/usr/bin/python3

''' 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
    Sample filename : abc.java 
    Output : java '''

flname = input("Enter a file name to find it\'s extension: ")
extn = flname.split('.')
print(repr(extn[-1]))


