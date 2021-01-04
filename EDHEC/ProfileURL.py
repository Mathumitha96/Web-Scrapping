import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:\\Users\\Bharathwaj\\Downloads\\chromedriver_win32\\chromedriver")
driver.maximize_window()
driver.get('https://alumni.edhec.edu/fr/')
sleep(1)
driver.find_element_by_xpath("//div[@id='edhec']/header/div/div/div/div/ul/li[8]/div/a").click()
#####################################
driver.find_element_by_name('login_s').send_keys('victoire.branger@edhec.com')
driver.find_element_by_name('pswd_s').send_keys('poi87UYT')
######################################
# driver.find_element_by_name('login_s').send_keys('thomas.charpier@edhec.com')
# driver.find_element_by_name('pswd_s').send_keys('Toto438!edh')
##################################################
sleep(0.5)
driver.find_element_by_xpath("//input[@value='Connexion']").click()
print("++++++++++++++++++++")
sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'Annuaire')]").click()
sleep(2)
print("++++Annuaire")
driver.find_element_by_link_text("Recherche avancée").click()
sleep(3)
print("+++++++Recherche")
driver.find_element_by_xpath("//*[@id='tarteaucitronPersonalize']").click()
sleep(5)
print("+++++++tarteaucitronPersonalize")
driver.find_element_by_xpath("//div[@id='zoneAnnuaire_layout']/div[3]/form/div[18]/div/input").click()
sleep(5)
button2 = driver.find_element_by_xpath('//div[@class="global-pagination"]//a[@data-page="2"]')
button2
driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",button2,'data-page' ,36)
button16 = driver.find_element_by_xpath('//div[@class="global-pagination"]//a[@data-page="36"]')
button16.click()
print("pagination")
links=[]
for x in range(0,3):   
    urls=driver.find_elements_by_xpath('//*[@class="click-img"]/a')  
    for url in urls:
        all_url=url.get_attribute('href')
        if '/profil' in all_url:
            links.append(all_url)
    driver.execute_script("window.scrollTo(0, 4)") 
    sleep(3)
    driver.find_element_by_link_text("Suivant").click()   
    sleep(7)
sleep(1)

with open('ProfileLinks36.csv', 'w', newline='') as csvFile:
	writer = csv.writer(csvFile, dialect='excel')
	for w in links:
		writer.writerow([w])
csvFile.close()

#driver.quit()
