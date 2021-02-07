import re
import csv
from time import sleep
import os
import sys
import pathlib
from timeit import default_timer as timer
import datetime

import urllib3
import instaloader

# Get instance
L = instaloader.Instaloader()

# Login or load session
################################################################################@



L.login('my_username', 'password')        # (login)
#L.interactive_login(USER)      # (ask password on terminal)
# L.load_session_from_file('dslr.lover.nepal') # (load session created w/
################################################################



## pathlib.Path('downloads/').mkdir(parents=True, exist_ok=True)  JSP

http = urllib3.PoolManager()

######################################




    print('\n\nGetting followers from',pro)


        
    
    profile = instaloader.Profile.from_username(L.context, pro)
    main_followers = profile.followers
    count = 0
    total=0
        # Print list of followees
    for person in profile.get_followers():
        try:
            total+=1
            username = person.username

            print('Username:',username)

            self.scrapped_list.append(username)

                print('--------------------------------------------------------------------------------\nTotal followers scraped:',total,' out of',main_followers)
                print('Current Account:',ind+1,'\t Remaining Accounts:',len(PROFILE)-ind-1 ,'\nAccount Name:',pro)
                
            
            except Exception as e:
                print(e)
            

        #saving the last account for resume
        f=open('last.txt','w+')
        f.write(pro)
        f.close()
        #log of completed account
        f=open('completed.txt','a+')
        f.write(pro+'\n')
        f.close()
        # (likewise with profile.get_followers())
    except:
        print('Skipping',pro)




class InstagramScrapper():
    def __init__(self,target_account,nb_profile,username,password):
        
        self.nb_profile = nb_profile
        self.L = instaloader.Instaloader()
        self.L.login(username, password)    #### se log    
        self.http = urllib3.PoolManager()
        self.pro = target_account

    def scrape(self):
        self.scrapped_list = list()


        pass