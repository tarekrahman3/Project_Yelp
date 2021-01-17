from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options, executable_path='/home/tarek/Selenium_Projects/chromedriver')

col1 =[]
col2 =[]

pages = (
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Augusta%2C%20GA',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Augusta%2C%20GA&start=10',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Augusta%2C%20GA&start=20',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Columbus%2C%20GA&start=0',
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Columbus%2C%20GA&start=10'
)
for page in pages:
	driver.get(page)
	time.sleep(5)
	ques = driver.find_elements_by_xpath('//ul/li/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')
	for que in ques:
		name = que.text
		col1.append(name)
		link = que.get_attribute("href")
		col2.append(link)
		print(f"Completed: {name}")
driver.quit()

data = {'name':  col1,
        'link': col2
        }
df = pd.DataFrame (data, columns = ['name','link'])
df.to_csv (r'export_search_results.csv', index = False, header=True)
print (df)

