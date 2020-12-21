#let's code loops!
#Task 2:
#Write a python program to print all positive numbers in a range

list1=[]
list2=[]
n=int(input('enter number of elements: '))
i=0
while i<n:
    num=int(input())
    list1.append(num)
    i=i+1

print('Input list: ',list1)

for j in list1:
    if(j>0):
      list2.append(j)

print('Output list: ',list2)


'''
Output:

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: C:/Users/HP/Desktop/Python/lets code loops/positiveNum.py ======
enter number of elements: 5
-3
11
55
-67
43
Input list:  [-3, 11, 55, -67, 43]
Output list:  [11, 55, 43]
>>>
'''
