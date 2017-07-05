#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

j=input("enter a number to find its prime factor(s)\n")
prime=[]

for a in range(2,10):
        k=j%a
        print "\-",a,"\-"
        if (k==0):
            if (a/2==0):
                prime.append(a)
        
print prime
