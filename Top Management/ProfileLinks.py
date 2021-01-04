import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
writer = csv.writer(open('urlAff.csv','w+',encoding='utf-8',newline=''))



driver = webdriver.Chrome('C:\\Users\\Bharathwaj\\Downloads\\chromedriver_win32\\chromedriver')
driver.get('https://www.topmanagement.fr/')
sleep(0.5)
connexion = driver.find_element_by_xpath('//li[@id="menu-item-144326"]/a')
connexion.click()
sleep(0.5)

username = driver.find_element_by_id('xoo-el-username')
sleep(1)
username.send_keys('benoit.feytit@metro.fr')
sleep(0.5)

password = driver.find_element_by_name('xoo-el-password')
password.send_keys('6F54D137F')
sleep(0.5)
print("---------------")
sign_in_button = driver.find_element_by_xpath('//button[contains(.,"Se connecter")]').click()
print("++++++++++++++++++++")
sleep(1)
#sign_in_button.click()
sleep(0.5)

print(1)
driver.get('https://www.topmanagement.fr/')
driver.get('https://topmanagement.fr/?s=Affaire')
sleep(3)

print(2)
urls = driver.find_elements_by_xpath('//a[contains(text(),"Voir sa biographie")]')
topmgmt_urls = [url.get_attribute('href') for url in urls]
sleep(0.5)
print(12)

for url in topmgmt_urls:

   # get the profile URL 
    driver.get(url)
    print(url)

    writer.writerow([url])





driver.quit()





