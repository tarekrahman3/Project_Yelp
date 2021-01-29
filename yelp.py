#URL = 'https://www.yelp.com/search?find_desc=pet%20boarding&find_loc=Mobile%2C%20AL'
URL = input("Enter Yelp Search URL: ")

from selenium import webdriver
import time
import csv
import os
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, executable_path='/home/tarek/Selenium_Projects/webdrivers/chromedriver')

col1 =[]
col2 =[]


def retrieve():
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//ul/li/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')))
	ques = driver.find_elements_by_xpath('//ul/li/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')
	for que in ques:
		name = que.text
		link = que.get_attribute("href")
		col1.append(link)
		col2.append(name)
		print(f"Completed: {name}")
def page_navigation():
	next_page = driver.find_element_by_xpath("//a[contains(@class, 'next-link navigation-button')]")
	next_page.click()
	WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul/li/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')))

def data_frame():
	data = {'links': col1,
		'name':  col2
		}
	df = pd.DataFrame (data, columns = ['links', 'name'])
	df.to_csv (r'search_results_gather_inspect_data.csv', index = False, header=True)
	df2 = pd.DataFrame (data, columns = ['links'])
	df2.to_csv (r'yelp_main_import_data.csv', index = False, header=True)
	print (df)

driver.get(URL)
while True:
	retrieve()
	try:
		page_navigation()
	except:
		break
data_frame()
print(f"||||||||||ITEM LENGTH = {len(col1)}")

def main_sequence():
	col1 =[]
	col2 =[]
	col3 =[]
	col4 =[]
	col5 =[]
	col6 =[]
	col7 =[]
	col8 =[]
	col9 =[]
	col10 =[]

	df = pd.read_csv('yelp_main_import_data.csv', header=0)
	links = df.links.to_list()

	for link in links:
		time.sleep(2)
		driver.get(link)
		time.sleep(4)
		col10.append(link)
		
		try:
			title = driver.find_element_by_xpath('//div/div/div[1]/h1').text
		except:
			title = "N/A"
		col1.append(title)
		try:
			website = driver.find_element_by_xpath('//section[1]/div/div[1]/div/div[1]/p[2]/a').text
		except:
			try:
				website = driver.find_element_by_xpath('//section[2]/div/div[1]/div/div[1]/p[2]/a').text
			except:
				website = 'N/A'
		col2.append(website)
		try:
			phone = driver.find_element_by_xpath('//section[1]/div/div[2]/div/div[1]/p[2]').text
		except:
			try:
				phone = driver.find_element_by_xpath('//section[2]/div/div[2]/div/div[1]/p[2]').text
			except:
				try:
				        phone = driver.find_element_by_xpath('//section[1]/div/div[1]/div/div[1]/p[2]').text
				except:
				        phone = 'N/A'
		col3.append(phone)
		try:
			address = driver.find_element_by_xpath('//address/p').text
		except:
			address = 'N/A'
		col4.append(address)
		try:
			city_state = driver.find_element_by_xpath('//address/p[3]/span').text
		except:
			try:
				city_state = driver.find_element_by_xpath('//address/p[2]/span').text
			except:
				try:
				        city_state = driver.find_element_by_xpath('//address/p').text
				except:
				        city_state = 'N/A'
		col5.append(city_state)
		try:
			owner = driver.find_element_by_xpath('//section[7]/div[2]/div[1]/div/div/div[2]/p').text
		except:
			try:
				owner = driver.find_element_by_xpath('//section[5]/div[2]/div[1]/div/div/div[2]/p').text
			except:
				try:
				        owner = driver.find_element_by_xpath('//section[6]/div[2]/div[1]/div/div/div[2]/p').text
				except:
				        owner = 'N/A'
		col6.append(owner)
		try:
			rating = driver.find_element_by_xpath('//div/div/div[2]/div[1]/span/div').get_attribute('aria-label')
		except:
			rating = 'N/A'
		col7.append(rating)
		try:
			rating_count = driver.find_element_by_xpath('//div/div/div[2]/div[2]/span').text
		except:
			rating_count = 'N/A'
		col8.append(rating_count)
		try:
			features = driver.find_element_by_xpath('//div/div[3]/div[1]/div[1]/div/div/span[2]').text
		except:
			try:
				features = driver.find_element_by_xpath('//*[@id="wrap"]//div/div/span[2]').text
			except:
				features = 'N/A'
		col9.append(features)
		print(f"{len(col10)} : {title}")
	driver.quit()
	data = {'source':  col10,
		'title':  col1,
		'website': col2,
		'phone': col3,
		'address': col4,
		'city_state': col5,
		'owner': col6,
		'rating': col7,
		'rating_count': col8,
		'features': col9
		}

	df = pd.DataFrame (data, columns = ['source','title','website','phone','address','city_state','owner','rating','rating_count','features'])
	df.to_csv (r'yelp_main_export_data.csv', index = False, header=True)

	print (df)
main_sequence()
