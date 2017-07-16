#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#for n in range(2520,5000):

import time
start = time.time()

for n in range(12252240,50000000):
    for i in range(2,21):   
        if n%i==0:
            i+=1
            if n%i==0:
                i+=1
                if n%i==0:
                    i+=1
                    if n%i==0:
                        i+=1
                        if n%i==0:
                            i+=1
                            if n%i==0:
                                i+=1
                                if n%i==0:
                                    i+=1
                                    if n%i==0:
                                       i+=1
                                       if n%i==0:
                                            i+=1
                                            if n%i==0:
                                                i+=1
                                                if n%i==0:
                                                    i+=1
                                                    if n%i==0:
                                                       i+=1
                                                       if n%i==0:
                                                            i+=1
                                                            if n%i==0:
                                                                #15
                                                                i+=1
                                                                if n%i==0:
                                                                    i+=1
                                                                    if n%i==0:
                                                                        i+=1
                                                                        if n%i==0:
                                                                            i+=1
                                                                            if n%i==0:
                                                                                i+=1
                                                                                print n,i


end = time.time()
print(end - start)
