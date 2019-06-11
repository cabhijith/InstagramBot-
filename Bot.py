


from selenium import webdriver

from time import sleep
import pickle

#All are standard Python modules except Selenium. Use 'pip install selenium' to download it
#You will also have to download Chromedriver for it to work on Chrome. Download it here - http://chromedriver.chromium.org/downloads
#------------------------------------------------------------------------------------------------------------------------------

chromedriver_path = 'C:/Users/absis/Downloads/chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

#The LogginIn function logs into Instagram with your credentials

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

    LoggingIn ('Enter', 'Enter')

#-----------------------------------------------------------------------------------------------------------------------
with open('followers_list_new', 'rb') as f:
    followers_list= pickle.load(f)

print(followers_list)

#----------------------------------------------------------------------------------------------------------------------

tgs = ['mothersday']

followers_count =  0
like_counter = 0
tags_count = -1
for tags in tgs:
    tags_count += 1
    webdriver.get ('https://www.instagram.com/explore/tags/' + tgs[tags_count])
    sleep (5)
    image = webdriver.find_element_by_css_selector(' #react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div._9AhH0')
    image.click()

    
    
    
    for x in range(1,15):   
        

        #To_Like_A_picture
        like = webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > span')
        like.click()
        like_counter += 1
        sleep(2)
        nextt = webdriver.find_element_by_css_selector(' body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a.HBoOv.coreSpriteRightPaginationArrow')
        nextt.click()
        sleep(8)
     
        
        
        if webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button').text == 'Follow':
            webdriver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button').click()
            sleep(8)
            usermane = webdriver.find_element_by_css_selector(' body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > h2 > a').text
            followers_list.append(usermane)
        else:
            print ('Already Following')


number_of_followers = len(followers_list)
print ('I followed these many people :: ', followers_count)

for x in followers_list:
    number_of_followers -= 1 
    print ('I followed', followers_list[number_of_followers])
    

with open('followers_list_new', 'wb') as f:
    pickle.dump(followers_list, f)
     



print ('In this cycle, I liked', like_counter, 'pictures!')    
with open('followers_list_new', 'rb') as f:
    followers_list= pickle.load(f)

print(followers_list)



