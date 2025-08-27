first_name = "Abinash"
last_name = "Behera"
full_name = "Abinash Behera"
country = "India"
city = "Bangalore"
age = 20
year = 2025
is_married = "No"
is_true = False
is_light_on = "Yes"
a, b = "hey", "you"

print(type(first_name))
print(type(age))
print(type(is_married))
print(type(is_light_on))
print(type(a))
print(type(b))
print(len(first_name))
print(len(last_name))
if len(first_name) > len(last_name):
    print("first_name greater in length")
else:
    print("last_name greater in length")

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
product = num_two * num_one
division = num_one/num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = 25 // 3
print(floor_division)
radius = 30
import math
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
radius = int(input("enter radius of circle: "))
area = math.pi * radius ** 2

first_name = input("enter first name: ")
last_name = input("enter last name: ")
country = input("enter country: ")
age = int(input("enter age: "))

## OUTPUT:
"""<class 'str'>
<class 'int'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
7
6
first_name greater in length
9
8
enter radius of circle: 30
enter first name: shiro
enter last name: nahara
enter country: japan
enter age: 4"""