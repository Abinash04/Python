
    

#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
max = 1000  
result = 0
for i in range(0,max):
    if i%3 == 0 or i%5 == 0:
        result += i

print "Sum of multiples of 3 and 5 upto the number less than 1000 is",result
