#1st Python Project
#Basic School Administration Tool
#

import csv      #for file ops on a csv file(as we will be storing data into an csv file)

def write_into_csv(info_list):
    #with open('student_info.csv', 'w+',newline='') as csv_file:        #here w+ will overwrite the file
    with open('student_info.csv', 'a',newline='') as csv_file:          #a append 
        #here csv_file is a variable holding the file object
        writer=csv.writer(csv_file)    #writer is an obj

        if csv_file.tell()==0:
            writer.writerow(['Name','Age','ContactNumber','Email-id'])

        writer.writerow(info_list)       #will write input given into csv file
        #writerow() function needs arg in form of 'List'
        #that's the reason we did 'split'
    
    


if __name__ == '__main__':
    condition=True          #entry point of code
    student_num=1           #to keep count of entries
    

    while condition:
        student_info=input('Enter student info for student #{} in following format(Name Age Contact_Number E-mail): '
                           .format(student_num))
        #print('Entered info: ',student_info)

        #split
        student_info_list=student_info.split(' ')
        #print('Split up is: ',student_info_list)

        print('\nThe entered informatiob is-\nName: {}\nAge: {}\nContactNumber: {}\nEmail-ID: {}'
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        entry_check=input('Is entered information correct? (yes/no): ')

        if entry_check=='yes':
            write_into_csv(student_info_list)
        
            condition_chk=input('Enter (yes/no) if you want to enter information of another student: ')
            if condition_chk=='yes':
                condition==True
                student_num=student_num+1
            elif condition_chk=='no':
                condition=False
        elif entry_check=='no':
            print('\nPlease re-enter thr values! ')

        
'''
Output:

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:\Users\HP\Desktop\Python\Project1\admin.py ============
Enter student info for student #1 in following format(Name Age Contact_Number E-mail): atharv 8 9787654321 atharv@yahoo.com

The entered informatiob is-
Name: atharv
Age: 8
ContactNumber: 9787654321
Email-ID: atharv@yahoo.com
Is entered information correct? (yes/no): yes
Enter (yes/no) if you want to enter information of another student: no
>>>
'''












