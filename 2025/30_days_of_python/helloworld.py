print(2 + 4) # addition (+)
print(2 - 4) # subtraction (-)
print(2 * 9) # multiplication (*)
print(4 / 8) # division (/) float - fraction
print(2 ** 3)# exponential (**)
print(2 % 3) # modulus (%) # remainder
print(4 // 3) # floor division (//) # quotient

# checking datatypes
print(type(10)) # int
print(type(10.34)) # float
print(type(10 + 4j)) # complex 
print(type("10")) # string
print(type([10, 34])) # list
print(type({"id":10, "name": "shiro"})) # dictionary
print(type({10, 34})) # set
print(type((10, [3,4]))) # tuple
print(type(10 > 3)) # bool
print(type(10 == 10)) # bool

##################################
# practice
##################################
print(4 // 9)
print(5 % 4)
print(45 // 34)
print(45 % 23)
print(7/9)

## tricky interview question
print((0.1 + 1.4) == 1.5)
print(0.3 + 0.6 == 0.9)
print(0.1 + 0.2)   # 0.30000000000000004
print(0.3)         # 0.3
print(0.1 + 0.2 == 0.3)   # False
print(2.4 + 1.2 == 3.6)   # False
print(1.5 + 2.25 == 3.75)   # True


"""Interview takeaway:

Never trust direct float equality (==) in critical code.

Use a tolerance check with math.isclose:"""
import math
print(math.isclose(0.1+0.2, 0.3))

"""convert a given floating number to python's 64-bit IEEE 754 double precision format"""
a = 5.75
"""computer understands only 0s and 1s, so to display the fraction into binary format, we will need to convert this float into binary format.
64 bits is nothing but 64 slots for 0s and 1s
[sign (1 - bit)][exponent (11 bits)][fraction/mantissa (52 bits)]

5.75

step1: plain binary (base -2) of 5.75
convert the integer part first i.e 5.
to convert an integer into binary format we divide by 2.
5 % 2 = 1 - remainder | 2 - Qutient
2 % 2 = 0 - remainder | 1 - Quotient
1 % 2 = 1 - remainder | 0 - Quotient
so from bottom to top --> 101 

now fraction part 0.75
to convert fraction part we multiply by 2.
0.75 x 2 = 1.5 - take first integer 1 and keep .50
0.50 x 2 = 1.0 - take first intger 1 and keep .00 (stop)
Fraction bits = 0.11

step2: IEEE 754 double (64-bit) representation of 5.75
a) normalize
5.75 = 101.11 (binary format)

to normalize move the decimal to  places left i.e. 1.0111 x 2^2 (to the power 2)
b) Fields
- sign (0 as positive)
- exponent ( actual exponent is 2 , stored biased by 1023 i.e. 2 + 1023 = 1025)
1025 in binary bits (11 bits) = 10000000001
- matissa (fraction): the bits after the leading 1 i.e. decimal part --> 0.111
0111-> followed by 52 bits (zero filled)
0111000000000000000000000000000000000000000000000000
c) concatenate
0|10000000001|0111000000000000000000000000000000000000000000000000

0100000000010111000000000000000000000000000000000000000000000000

64-bit for 5.75 will be stored as 0100000000010111000000000000000000000000000000000000000000000000
"""

b = 10.25
# find binary of 10
"""10 % 2 = 0 | 5
5 % 2 = 1 | 2
2 % 2 = 0 | 1
1 % 2 = 1 | 0"""
# binary for 10 is 1010
# find binary for fraction .25
""".25 x 2 = 0.5, take 0 and keep 0.5
0.5 x 2 = 1.0, take 1 and keep .00(stop)
take it from top down"""
## fraction bits for .25 is .01

# normalize 1010.01 - move the decimal after first integer i.e. 3 digit towards left so 1.01001 x 10^3
# 0.10 x 2^0
# Fields
"""1 - bit --> 0 - positive
11 - exponent --> actual exponent is 3 as we moved the decimal places to 3, 3 + 1023 = 1026 (exponent=3)
binary for 1026 is 10000000010
# mantessa (fraction) --> .01001
0|10000000010|01001<followed_by_ 52-5 zero filled>
0100000000100100100000000000000000000000000000000000000000000000"""

"""Single precision (32-bit):

1 bit → sign

8 bits → exponent

23 bits → fraction (mantissa)

~ 7 decimal digits of precision

Double precision (64-bit):

1 bit → sign

11 bits → exponent

52 bits → fraction (mantissa)

~ 15–16 decimal digits of precision"""

"""If the fraction part is a power of 2 denominator (like 0.5 = 1/2, 0.25 = 1/4, 0.75 = 3/4), it has an exact binary representation.
✅ So numbers like 1.5, 2.25, 3.75 are exact — their sums compare cleanly.

If the fraction part is something like 0.1, 0.2, 0.3, 0.4, 0.6, etc. (anything that’s a fraction with denominator involving 2 and 5 in decimal, like 1/10, 2/10, 3/10…), it cannot be represented exactly in binary."""
## OUTPUT##
"""6
-2
18
0.5
8
2
1
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'set'>
<class 'tuple'>
<class 'bool'>
<class 'bool'>
0
1
1
22
0.7777777777777778
True
False
0.30000000000000004
0.3
False
False
True
True"""