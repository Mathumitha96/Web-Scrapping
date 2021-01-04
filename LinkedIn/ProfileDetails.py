from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


from itertools import zip_longest

import csv

import time

import io



list_of_links = []
list_of_emails = []
list_of_ConnectionsFName = []
list_of_ConnectionsMName = []
list_of_ConnectionsLName = []
list_of_Connected_Time = []
list_Of_Companies = []
connectionName = ""
emailText = ""
connectedTime = ""
companyName = ""

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

time.sleep(5)

with open('D:/Python/LinkedIn/300.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		list_of_links.append(', '.join(row))



for link in list_of_links:
	print(link)
	try:
		driver.get(link)
		time.sleep(5)
	except TimeoutException:
		driver.refresh()
		
	try:
		companyName = driver.find_element_by_xpath("//ul[@class = 'pv-top-card--experience-list']//a[@class='pv-top-card--experience-list-item']//span").text
	except NoSuchElementException:
		companyName = ""
	time.sleep(5)
	try:
		driver.find_element_by_xpath('//a[@data-control-name="contact_see_more"]').click()
	except NoSuchElementException:
		#print('not clicked once')
		driver.refresh()
		time.sleep(5)
		try:
			driver.find_element_by_xpath('//a[@data-control-name="contact_see_more"]').click()
		except NoSuchElementException:
			#print('not clicked twice')

			try:
				driver.find_element_by_xpath('//p[@class="signin-link"]//a[@class="sign-in-link"]').click()
				print('Clicked Signin')
				time.sleep(5)
				username = driver.find_element_by_id('username')
				username.send_keys('antoine@hello-pomelo.fr')
				pswd = driver.find_element_by_id('password')
				pswd.send_keys('Pomelo2017')
				log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
				log_in_button.click()
				#print('Clicked Login')
				time.sleep(5)
				companyName = driver.find_element_by_xpath("//ul[@class = 'pv-top-card--experience-list']//a[@class='pv-top-card--experience-list-item']//span").text
				print(companyName)
				driver.find_element_by_xpath('//a[@data-control-name="contact_see_more"]').click()
				#print('Clicked contact')
				time.sleep(5)
			except NoSuchElementException:
				#print('not clicked thrice')
				companyName =""
				try:
					driver.find_element_by_xpath("li-icon[@type='linkedin-bug']")
					driver.refresh()
				except NoSuchElementException:
					print('not refreshed')
					break


	time.sleep(5)
	try:
		#emailText = driver.find_element_by_xpath("//section[@class = 'pv-contact-info__contact-type ci-email']//div[@class = 'pv-contact-info__ci-container']//a[@rel='noopener noreferrer']").text
		emailText = driver.find_element_by_xpath("//section[@class = 'pv-contact-info__contact-type ci-email']//div[@class = 'pv-contact-info__ci-container t-14']//a[@rel='noopener noreferrer']").text
		#print('emailText')
		print(emailText)
	except NoSuchElementException:
		#print("gone for exception")
		emailText = "";

	try:
		connectionName = driver.find_element_by_xpath("//div[@class='artdeco-modal__header ember-view']//h1[@id='pv-contact-info']").text
	except NoSuchElementException:
		connectionName = "";
	
	try:
		connectedTime = driver.find_element_by_xpath("//section[@class = 'pv-contact-info__contact-type ci-connected']//div[@class = 'pv-contact-info__ci-container t-14']//span").text
		#print('connectedTime')
		print(connectedTime)
	except NoSuchElementException:
		connectedTime = "";

	
	list_of_emails.append(emailText)
	list_of_Connected_Time.append(connectedTime)
	list_Of_Companies.append(companyName)
	lst = connectionName.split(' ')
	list_of_ConnectionsFName.append(lst[0])
	if len(lst) == 3 or len(lst)>3:
		list_of_ConnectionsMName.append(lst[1])
		list_of_ConnectionsLName.append(lst[2])
	elif len(lst)<3:
		if len(lst)<2:
			list_of_ConnectionsMName.append(' ')
			list_of_ConnectionsLName.append(' ')
		else:
			list_of_ConnectionsMName.append(' ')
			list_of_ConnectionsLName.append(lst[1])
	print(connectionName+" "+emailText+" "+connectedTime+" "+companyName)
	#print(emailText)

import unicodecsv as csv, re

with open('1to300.csv', 'wb') as csvFile:
	writer = csv.writer(csvFile, encoding='utf-8')
	writer.writerow(['First Name','Middle Name','Last Name','Email','Connected','Company Name'])
	for u, v, w, x, y, z in zip_longest(list_of_ConnectionsFName,list_of_ConnectionsMName,list_of_ConnectionsLName, list_of_emails,list_of_Connected_Time,list_Of_Companies):
		writer.writerow([u, v, w, x, y, z])
csvFile.close()