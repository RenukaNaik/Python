#let's code loops!
#Task 1:
#Write a python program for fibonacci numbers


n=int(input('Enter the term: '))
n1=0
n2=1
i=0
if n<=0:
    print('Please enter positive number.')
else:
    print('Fibonacci sequence for',n,'is: ')
    for i in range(n):
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
        i=i+1

        
'''
Output:

======= RESTART: C:/Users/HP/Desktop/Python/lets code loops/fibonacci.py =======
Enter the term: 15
Fibonacci sequence for 15 is: 
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
>>>
'''
