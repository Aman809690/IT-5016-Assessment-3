"""
program which calcluate the radius of a circle , given the area 
author: Aman
"""
import math
area= float(input("enter the value:"))
radius=math.sqrt(area/math.pi)
print("radius of circle",radius)