import instaloader

class InstagramScrapper():
    def __init__(self,target_account,nb_profile,username,password):
        
        self.nb_profile = nb_profile
        self.L = instaloader.Instaloader()
        self.L.login(username, password)    #### se log    
        ##self.http = urllib3.PoolManager()
        self.pro = target_account
        self.profile = instaloader.Profile.from_username(self.L.context, self.pro)
        self.main_followers = self.profile.followers

    def scrape(self):
        self.scrapped_list = list()
        for person in self.profile.get_followers():
            self.scrapped_list.append(person.username)
            if len(self.scrapped_list) >= self.nb_profile:
                break
            #print(person.username)
        #print(type(self.profile.get_followers()))

#my_username = input('My Username : ')
#password = input('My Password : ')
#target_username = input("target username : ")
#scrapper = InstagramScrapper(target_username,30,my_username,password)
#scrapper.scrape()
#print (scrapper.scrapped_list)
#print(len(scrapper.scrapped_list))