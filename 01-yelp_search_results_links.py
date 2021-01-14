from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options, executable_path='/home/tarek/Selenium Projects/chromedriver')

rows = []

pages = (
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Raleigh%2C%20NC&ns=1&start=50',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Raleigh%2C%20NC&ns=1&start=60',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Raleigh%2C%20NC&ns=1&start=70',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Raleigh%2C%20NC&ns=1&start=80',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Raleigh%2C%20NC&ns=1&start=90'
)
for page in pages:
	driver.get(page)
	time.sleep(5)
	ques = driver.find_elements_by_xpath('//ul/li/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')
	for que in ques:
	 name = que.text
	 link = que.get_attribute("href")
	 row = [name + ',' + link]
	 rows.append(row)

for data in rows:
    print(data)

