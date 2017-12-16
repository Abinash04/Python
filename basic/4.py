#!/usr/bin/python
'''4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output : 
    r = 1.1
    Area = 3.8013271108436504'''

import math as m
r = float(input ("Enter a radius value for the circle:"))
#area = m.pi * pow(r,2)
print ("Area of circle with radius " +str(r) + " is: "  + str(m.pi * pow(r,2)))

