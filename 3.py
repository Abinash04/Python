#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

z="largest prime factor of the number 600851475143\n"
print z

def prime_factor(z):
	n = z
	prime = 2
	while True:
		if n % prime != 0:
			prime += 1
		else:
			n = n / prime
		
		if n == prime:
			return prime
			break

print prime_factor(600851475143)


        
