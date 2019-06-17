from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep, strftime
from random import randint
import pandas as pd
import pickle 
#------------------------------------------------------------------------------------------------------------------------------

chromedriver_path = 'C:/Users/absis/Downloads/chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

def LoggingIn (user, passs):
    username = webdriver.find_element_by_name('username')
    username.send_keys(user)

    password = webdriver.find_element_by_name('password')
    password.send_keys(passs)

    sleep (3)

    login_form = webdriver.find_element_by_xpath('//*[@id= "react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
    login_form.click()

    sleep(3)

    notif = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notif.click()

LoggingIn ('username', 'password')

#-----------------------------------------------------------------------------------------------------------------------
with open('followers_list_new', 'rb') as f:
    followers_list= pickle.load(f)

print(followers_list)

#----------------------------------------------------------------------------------------------------------------------
start_time = time.time()

tgs = ['hacking', 'code', 'python', 'programmar']
Commenting_adjectives = ['Awesome', 'Magnificent', 'Great', 'breathtaking', 'amazing', 'stunning', 'astounding', 'astonishing', 'awe-inspiring', 'stupendous', 'staggering', 'extraordinary', 'incredible']
#geo-tags = 213480180/washington-district-of-columbia/

followers_count =  0
likes_count = 0
tags_count = -1
comments_count = 0
min_likes = 10 #Modify this to set the minimum number of likes on a post for you to comment on it


for tags in tgs:
    tags_count += 1
    webdriver.get ('https://www.instagram.com/explore/tags/' + tgs[tags_count])
    #webdriver.get ('https://www.instagram.com/explore/locations/'+ geo-tags[tags_count])
    sleep (5)
    image = webdriver.find_element_by_css_selector(' #react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div._9AhH0')
    image.click()
    sleep(7)
    
    if randint(1,10) > 1:
    
        for x in range(1,2):   
            

            #To_Like_A_picture
            like = webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > span')
            like.click()
            likes_count += 1
            sleep(2)
            nextt = webdriver.find_element_by_css_selector(' body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a.HBoOv.coreSpriteRightPaginationArrow')
            nextt.click()
            sleep(8)

            bookmarking = webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.wmtNn > button > span').click()
             
            if randint(1,10) > 1:
            #To Follow a Person
                if webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button').text == 'Follow':
                    webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button').click()
                    sleep(8)
                    usermane = webdriver.find_element_by_css_selector(' body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > h2 > a').text
                    followers_list.append(usermane)
                    followers_count += 1

                else:
                    print ('Already Following')
                
                sleep(4)
            else:
                print('Not following this person. SKIPPING IT')

            #For Commenting on Pictures
            try:
                if randint(1,10) > 1:
                    like = webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div > button').text
                    number_of_likes = int(like.split()[0].replace(',', ''))
                    
                    sleep(5)
                    
                    webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button > span').click()
                    sleep(5)
                    comment_area = webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea')
                    
                    comments_count += 1
                    if number_of_likes > min_likes and number_of_likes <1000:
                        comment_area.send_keys(Commenting_adjectives[randint(0, len(Commenting_adjectives) - 1)] ,' Pic!  Follow back for ', Commenting_adjectives[randint(0, len(Commenting_adjectives) - 1)], "  content:)")
                        sleep(3)
                    elif number_of_likes > 1000:
                        comment_area.send_keys("Follow us for memes and other awesome content ")
                        sleep(3)
                    else:
                         continue

        
                    



                    comment_area.send_keys(Keys.ENTER)
                else:
                    print('Not COMMENTING on this person. SKIPPING IT')
            except:
                continue
        else:
            print('We are skipping this one!')





number_of_followers = len(followers_list)
print ('In this cycle', followers_count, 'were followed')
print ('In this cycle', likes_count, 'pictures were liked!')    
print ('In this cycle,',comments_count,'comments were made' )

for x in followers_list:
    number_of_followers -= 1 
    print ('Till now I have followed', followers_list[number_of_followers])
    

with open('followers_list_new', 'wb') as f:
    pickle.dump(followers_list, f)
     


with open('followers_list_new', 'rb') as f:
    followers_list= pickle.load(f)

print(followers_list)

print("It took these many minutes" , (time.time() - start_time/ 60))



