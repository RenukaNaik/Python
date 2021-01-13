#databases(web scraping project)
#

import sqlite3

def connect(dbname):
    #create db or make connection to db if alreadt exists
    #conn=sqlite3.connect('flip.db')
    conn=sqlite3.connect(dbname)
    conn.execute('CREATE TABLE IF NOT EXISTS MOBILES (NAME TEXT,RATINGS TEXT,PRICE TEXT,FEATURES TEXT)')
    print('Table created successfully...')

    conn.close()

def insert_into_table(dbname,values):
    conn=sqlite3.connect(dbname)
    print('Inserted into table: '+ str(values))
    insert_sql = "INSERT INTO MOBILES (NAME,RATINGS,PRICE,FEATURES) VALUES (?,?,?,?)"
    conn.execute(insert_sql,values)
    conn.commit()   #to make sure db is in stable condition
    
    conn.close()
#in above function--> values has to be a tuple
    #and has to be in same order

def get_info(dbname):
    conn=sqlite3.connect(dbname)
    cur= conn.cursor()
    cur.execute('SELECT * FROM MOBILES')

    table_data=cur.fetchall()

    for record in table_data:
        print(record)
    conn.close()
