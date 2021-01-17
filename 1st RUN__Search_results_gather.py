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
'https://www.yelp.com/search?find_desc=Pet%20Boarding&find_loc=Augusta%2C%20GA&start=10'
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
df.to_csv (r'search_results_gather_inspect_data.csv', index = False, header=True)
df2 = pd.DataFrame (data, columns = ['link'])
df2.to_csv (r'yelp_main_import_data.csv', index = False, header=False)
print (df)

