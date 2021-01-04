import csv
import re
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
list_of_links = []
fname=""
lname=""
email=""
phone=""
company=""
position=""
year=""
writer = csv.writer(open('ProfileDetails30.csv','w+',encoding='utf-8-sig',newline=''))
writer.writerow(['First Name','Name','Email','Phone','Company','Position','Class year'])

driver = webdriver.Chrome("D:/Python/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get('https://alumni.edhec.edu/fr')
driver.maximize_window()
sleep(1)
driver.find_element_by_xpath("//div[@id='edhec']/header/div/div/div/div/ul/li[8]/div/a").click()
#----------------------------------------------------
driver.find_element_by_name('login_s').send_keys('thomas.charpier@edhec.com')
driver.find_element_by_name('pswd_s').send_keys('Toto438!edh')
#----------------------------------------------------
# driver.find_element_by_name('login_s').send_keys('victoire.branger@edhec.com')
# driver.find_element_by_name('pswd_s').send_keys('poi87UYT')
#----------------------------------------------------
sleep(0.5)
driver.find_element_by_xpath("//input[@value='Connexion']").click()
print("++++++++++++++++++++")
sleep(3)

with open('C:/Users/mathu/ProfileLinks30.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		list_of_links.append(', '.join(row))
for link in list_of_links:
    try:
        driver.get(link)
        sleep(5)
    except TimeoutException:
        driver.refresh()

    try:
        name=driver.find_element_by_xpath("//*[@id='module_ep']/div[2]/div/div/div[1]/div/div[1]/div[2]/div[1]").text
        name_arr = name.split(" ", 1)
        fname = name_arr[0]
        lname = name_arr[1] if len(name_arr) > 1 else ""
    except NoSuchElementException:
        name=""
    print("The fname is ",fname)
    print("The lname is ",lname)

    try:
        position = driver.find_element_by_xpath("//div[@id='module_ep']/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/strong/i").text
    except:
        position=""
    print('the position is: ',position)
    try:
        company = driver.find_element_by_xpath("//div[@id='module_ep']/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/span/strong").text
    except:
        company=""
    print('the company is: ',company)
    try:
        email = driver.find_element_by_xpath(".//*[@id='adresse_perso_mail_tooltip']/a").get_attribute('href')
        mailto,mail = email.split(':',1)
    except:
        email=""
    print('the email is: ',mail)

    try:
        phone = driver.find_element_by_xpath(".//div[@id='adresse_perso_phone_tooltip']").get_attribute('innerHTML').strip()[5:-4]
    except:
        email=""
    print('the email is: ',mail)

    try:
        detail = driver.find_elements_by_xpath("//div[@id='module_ep']/div[2]/div/div/div/div/div/div[2]/div[2]")[0].text  
        year = re.sub("\D", "", detail)
    except:
        year=""
    print('The year  is',year)
    
    writer.writerow([fname,
                    lname,
                    mail,
                    phone, 
                    company,
                    position,                   
                    year])
driver.quit()
    

    