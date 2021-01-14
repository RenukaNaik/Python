#Challenge:Functions!
#Task 1:
#Write a python code to create a function called most_frequent that takes a sring
#and prints the letters in decreasing order of frequency. Use dictionaries.


d1={}
def most_frequent(str1):    
    for i in str1:
        if i in d1.keys():
            d1[i]+=1
        else:
            d1[i]=1
           
a=str(input('Please enter a string: '))
most_frequent(a)
print(d1)

sort=sorted(d1.items(),key=lambda x:x[1],reverse=True)

for i in sort:
    print(i[0],'=',i[1])


'''
Output:
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:/Users/Dell/Desktop/Python/functions/frequency.py =========
Please enter a string: mississippi
{'m': 1, 'i': 4, 's': 4, 'p': 2}
i = 4
s = 4
p = 2
m = 1
>>>
'''
