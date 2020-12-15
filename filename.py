#Let's code data structures
#Task 2:
#Write a Python Program to accept a filename from user and print extension of that

filename=input('Input the filename: ')
ex=filename.split('.')
#print('split:',ex)
#print(ex[-1])

dict={
    'py':'python',
    'txt':'text',
    'cpp':'c++'
    }
#print(dict.get(ex[-1]))

if ex[-1] in dict.keys():
    print('The extension of the file is: ',dict.get(ex[-1]))
else:
    print('The extension of the file is: ',ex[-1])

'''
Output:

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:/Users/HP/Desktop/Python/lets code data struct/filename.py ====
Input the filename: t.py
The extension of the file is:  python
>>> 
===== RESTART: C:/Users/HP/Desktop/Python/lets code data struct/filename.py ====
Input the filename: t.c
The extension of the file is:  c
>>>
'''
