
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle
#------------------------------------------------------------------------------------------------------------------------------

chromedriver_path = 'C:/Users/absis/Downloads/chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(7)

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





with open('followers_list_neww', 'rb') as f:
    mylist = pickle.load(f)

print(mylist)

number_of_followers = len(mylist)

for x in range(1,40 ):
   try: 
     number_of_followers -= 1

     webdriver.get('https://www.instagram.com/' + mylist[number_of_followers ])
     sleep(7)
     webdriver.find_element_by_css_selector('button').click()
     sleep(20)
     webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_').click()
     sleep(2)
     del mylist[number_of_followers]
   
   except:
    continue

with open('followers_list_neww', 'wb') as f:
    pickle.dump(mylist, f)
with open('followers_list_neww', 'rb') as f:
    mylist= pickle.load(f)
     

print(mylist)

