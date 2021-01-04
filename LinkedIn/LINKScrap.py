
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


from itertools import zip_longest

import csv

import time

t1 = time.localtime()
start_time = time.strftime("%H:%M:%S", t1)
print("Starting Time")
print(start_time)

options = Options()
options.max_duration = 10800
driver = webdriver.Chrome(chrome_options=options, executable_path="D:/Python/chromedriver_win32/chromedriver.exe")

driver.maximize_window()

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_id('username')

username.send_keys('antoine@hello-pomelo.fr')

pswd = driver.find_element_by_id('password')

pswd.send_keys('Pomelo2017')

log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

log_in_button.click()

#driver.find_element_by_xpath('//a[@class="full-width"]').click()
time.sleep(15)
driver.find_element_by_xpath('//li[@class="global-nav__primary-item"]//a[@data-alias="relationships"]').click()

time.sleep(10)

driver.find_element_by_xpath('//div[@class="mn-community-summary__sub-section artdeco-dropdown__item"]//a[@data-control-name="connections"]').click()

time.sleep(5)
i=0
try:
	last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	last_height = driver.execute_script("return document.body.scrollHeight")
	print(last_height)
	while i<85:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(5)
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			print('last_height')
			print(last_height)
			print('new_height')
			print(new_height)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(15)
			driver.execute_script("window.scrollTo(0, -250);")
			time.sleep(15)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(15)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(15)
			new_height = driver.execute_script("return document.body.scrollHeight")
			print('last_height')
			print(last_height)
			print('new_height')
			print(new_height)
			if new_height == last_height:
				print('Equal')
				break
		last_height = new_height
		i+=1
except:
	print('Exception')

print('i value')
print(i)
t3 = time.localtime()
scrollDown_End_time = time.strftime("%H:%M:%S", t3)
print("Scroll  down ending Time")
print(scrollDown_End_time)
time.sleep(5)

time.sleep(60)
links = [link.get_attribute('href') for link in driver.find_elements_by_xpath('//li[@class="mn-connection-card artdeco-list ember-view"]//div[@class="mn-connection-card__details"]//a[@data-control-name="connection_profile"]')]
#links2 = driver.find_elements_by_xpath('//div[@id="groupsMemberSection_recently_joined"]//div[@class="lists"]//div[@class="fbProfileBrowserResult hideSummary"]//div[@data-name="GroupProfileGrid"]//div[@class="fbProfileBrowserList expandedList"]')
#print(links2)

list_of_emails = []
list_of_ConnectionsFName = []
list_of_ConnectionsMName = []
list_of_ConnectionsLName = []
connectionName = ""
emailText = ""

#print(links1)
with open('LinkedInProfileLinksNew.csv', 'w', newline='') as csvFile:
	writer = csv.writer(csvFile, dialect='excel')
	for w in links:
		writer.writerow([w])
csvFile.close()

		



	





