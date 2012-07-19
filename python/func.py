# A function definition example
# Created by David - July 2012

import math

# Return the area of a circle 
# for a specified radius
def area_of_a_circle(radius):
   return math.pi * (radius*radius)

radius = input("Circle radius? ")
area = area_of_a_circle(radius)
print ("Area is ") + format(area)   