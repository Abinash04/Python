#By considering the terms in the Fibonacci sequence whose values do not exceed
#four million, find the sum of the even-valued terms.

def fibonacci(n):
    fib=[0,1]
    my_list=[]
    for i in range(2,n+1):
        fib.append(fib[-1]+fib[-2])
    for i in range(len(fib)):
        if (fib[i] <= 4000000) and (fib[i]%2==0):
            my_list.append(fib[i])
    print my_list
    total=sum(my_list)
    print total
            
m = input("enter a value for fibonacci series\n")
series=fibonacci(m)

