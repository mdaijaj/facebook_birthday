from selenium import webdriver 
import pprint, requests
from time import sleep 
from getpass import getpass
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import schedule
import time

option = Options()                          
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")      #"**--disable-notifications**"
option.add_argument("--disable-notifications")

username='8826616653'
password = "Aijaj@#786"

driver = webdriver.Chrome("./chromedriver", chrome_options=option)
url= 'https://www.facebook.com/'
driver.get(url) 
print ("Opened facebook") 
sleep(1) 
driver.maximize_window()
sleep(2) 

username_box = driver.find_element_by_id('email') 
username_box.send_keys(username) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(password) 
print ("Password entered") 

login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
sleep(10) 
print("login sucessfully!")



market_url= url+ 'events/birthdays/' 
driver.get(market_url)
sleep(5)


# veryement_by_name("passwd")

wish=driver.find_elements_by_class_name("_1mf._1mj")
wish[0].send_keys("Wish you very happy birthday and God bless and happy yourself!"  + "\n")
sleep(8)
print("message sent sucessfully!")
print(wish)


print("plz wait")
time.sleep(5)

def job():
    print("I'm working...")

schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
input('Press anything to quit') 
# driver.close()
driver.quit()





