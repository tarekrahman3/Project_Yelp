from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options, executable_path='/home/tarek/Selenium Projects/chromedriver')

rows = []

pages = (
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Greensboro%2C%20NC&start=0',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Greensboro%2C%20NC&start=10',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Greensboro%2C%20NC&start=20',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Greensboro%2C%20NC&start=30'
)
for page in pages:
	driver.get(page)
	time.sleep(5)
	ques = driver.find_elements_by_xpath('//ul/li/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')
	for que in ques:
		name = que.text
		link = que.get_attribute("href")
		try:
			rating = find_element_by_xpath('//div/div[1]/span/div').get_attribute('aria-label')
		except:
			rating = 'N/A'
		row = f"name: {name};,link: {link};,rating {rating}"
		rows.append(row)
		print(f"Completed: {name}")

for data in rows:
    print(data)
