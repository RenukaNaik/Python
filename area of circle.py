#Let's code data structures
#Task 1:
#Write a python program which accepts the radius of a circle from user and computes area

import math
r=float(input('Input the radius of circle: '))
area=math.pi*r**2       #area=pi*(r^2)
print('The area of hte circle with radius', r ,'is: ',area)

'''
Output:

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:/Users/HP/Desktop/Python/lets code data struct/area of circle.py =
Input the radius of circle: 1.1
The area of hte circle with radius 1.1 is:  3.8013271108436504
>>> 
== RESTART: C:/Users/HP/Desktop/Python/lets code data struct/area of circle.py =
Input the radius of circle: 4.5
The area of hte circle with radius 4.5 is:  63.61725123519331
>>>
'''
