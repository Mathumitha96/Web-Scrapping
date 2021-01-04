import csv
import time
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
society=""
fonction=""
email=""
'''nation=""
address="" '''
phone=""
writer = csv.writer(open('Sc1.csv','w+',encoding='utf-8-sig',newline=''))
writer.writerow(['First Name', 'Name','Society','Fonction', 'Email','Telephone'])


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
sleep(3)
#sign_in_button.click()


with open('C:/Users/HP/Desktop/urlSci.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		list_of_links.append(', '.join(row))

for link in list_of_links:
    
    try:
        print('kiiiiiiii',link)
        driver.get(link)
        time.sleep(5)
    except TimeoutException:
        driver.refresh()

    sel = Selector(text=driver.page_source)		
	
    #name = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[1]/div/h2').extract_first().split()

    #name= ' '.join(name)
    try:
        name=driver.find_element_by_xpath(".//div[contains(@class,'et_pb_title_container')]").text
        fname,lname=name.split(' ',1)
    except NoSuchElementException:
        name=""
   # name=driver.find_element_by_xpath(".//div[contains(@class,'et_pb_title_container')]").text


    print("The name is ",name)
#xpath=//a[contains(@href, 'mailto:s.perrot@cps-quality.com')]
    try:
        society = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[1]/a/text()').extract()[0]

    except:
        
        society=""

   # society = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[1]/a/text()').extract()

    #society= ' '.join(society)
    
    print('the Societ is: ',society)

    try:
        fonction = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[2]/text()').extract_first()[2:]
    except:
        fonction=""

  #  fonction = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[2]/text()').extract_first()

    #fonction= ' '.join(fonction)
    
    print('the Fonc is: ',fonction)
#xpath=//a[contains(@href)]
    #email = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[3]/a/text()').extract()
    try:
        email= driver.find_element_by_xpath(".//p[contains(@class,'email field')]/a").text
    except:
        email=""

   

    #email= ' '.join(email)
    
    print('the email is: ',email)
    '''try:
        nation = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[4]/text()').extract_first()[2:]
    except NoSuchElementException:
        nation=""

    #nation = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[4]/text()').extract_first()

    #nation= ' '.join(nation)
    
    print('the nation is: ',nation)

    #address = sel.xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[6]').extract_first()
    try:
        address=driver.find_elements_by_xpath(".//p[contains(@class,'adresse field')]")[0].text[25:]
    except:
        address=""

   # address=driver.find_elements_by_xpath(".//p[contains(@class,'adresse field')]")[0].text[25:]

    #address= ' '.join(address)
    
    print("The address is: ",address) '''

    try:
        phone = driver.find_elements_by_xpath(".//p[contains(@class,'telephone field')]/a")[0].text
    except:
        phone=""

    #phone = driver.find_elements_by_xpath(".//p[contains(@class,'telephone field')]/a")[0].text
    
    #phone=driver.find_element_by_xpath('//*[@id="et-boc"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/p[6]/').text
    #phone= ' '.join(phone)
    
    print('The phone num is',phone)
    writer.writerow([fname,
                    lname,
                    society,
                    fonction,
                    email,                    
                    phone])




driver.quit()



