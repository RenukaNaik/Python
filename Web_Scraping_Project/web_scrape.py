#Web Scraping Project
#
#


import requests
from bs4 import BeautifulSoup

#import pandas   #collect info-->store it into data struct-->put it in file
import argparse #for cmd line arg

import connect  #connect.py(python allows to import .py files in same folder)


parser= argparse.ArgumentParser()
parser.add_argument('--page_num_max', help='Enter the number of pages to parse', type=int)
parser.add_argument('--dbname', help='Enter the name of database to be created', type=str)
args=parser.parse_args()

url='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=clp_metro_expandable_6_20.metroExpandable.METRO_EXPANDABLE_iPhone_mobile-phones-store_92RED14GXPXF_wp16&fm=neo%2Fmerchandising&iid=M_4df7278f-f8c5-4300-82ed-fb6fe88cf7b9_20.92RED14GXPXF&ppt=clp&ppn=mobile-phones-store&ssid=iahds1asfk0000001610345075495&page='
#page_num_MAX=4
page_num_MAX=args.page_num_max
scraped_info_list=[]

connect.connect(args.dbname)    #db created

for page_num in range(1,page_num_MAX):
    print('GET request for: ' + url + str(page_num))
    req=requests.get(url + str(page_num))
    content=req.content

    #print(content)


    soup=BeautifulSoup(content,'html.parser')

    all_mobiles=soup.find_all('div',{'class':'_13oc-S'})
    #print(all_mobiles)
    


    for mobile in all_mobiles:
        mobile_dict={}
        mobile_dict['Name']=mobile.find('div',{'class':'_4rR01T'}).text
        #print(mobile_name)

        #try ... except (for smooth implementation of code if ant attr is not found )
        try:
            mobile_dict['Ratings']=mobile.find('span',{'class':'_2_R_DZ'}).text
        except AttributeError:
            mobile_dict['Ratings']=None
            #pass 
        #print(ratings)
        mobile_dict['Price']=mobile.find('div',{'class':'_30jeq3'}).text
        #print(price)
        

        feature_list=[]
        parent_features=mobile.find('div',{'class':'fMghEO'})
        for feature in parent_features.find_all('ul',{'class':'_1xgFaf'}):
            f=feature.find_all('li',{'class':'rgWa7D'})
            
            for i in f:
                list=i.text
                feature_list.append(list)
            #print(feature_list)    
        print()
        
        mobile_dict['Features']=',  '.join(feature_list)    
        #we cant store list in csv. Thus we use .join() to join list with comma and space

        scraped_info_list.append(mobile_dict)

        connect.insert_into_table(args.dbname,tuple(mobile_dict.values()))      #values has to be tuple
        
        #store all collected info in a list
        #as pandas process info in form of list
        #to do this-->take all collected info and convert it into dictionary


#dataFrame=pandas.DataFrame(scraped_info_list)              #data structure used by pandas lib
#print('creating csv file...')
#dataFrame.to_csv('Flipkart.csv')                #converts ds to csv file

      
connect.get_info(args.dbname)  






    

