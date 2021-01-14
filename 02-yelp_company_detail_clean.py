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

col1 =[]
col2 =[]
col3 =[]
col4 =[]
col5 =[]
col6 =[]
col7 =[]
col8 =[]
col9 =[]

companys = (
'https://www.yelp.com/biz/pet-palace-cary-cary?osq=Pet+Boarding',
'https://www.yelp.com/biz/dogevolve-durham-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/walk-and-wag-chapel-hill?osq=Pet+Boarding',
'https://www.yelp.com/biz/pure-love-pet-sitting-cary?osq=Pet+Boarding',
'https://www.yelp.com/biz/chapel-hill-pet-resort-chapel-hill?osq=Pet+Boarding',
'https://www.yelp.com/biz/cats-at-home-chapel-hill?osq=Pet+Boarding',
'https://www.yelp.com/biz/petsound-daycare-and-boarding-cary?osq=Pet+Boarding',
'https://www.yelp.com/biz/laughing-dog-pet-care-carrboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/brier-creek-pet-hotel-morrisville?osq=Pet+Boarding',
'https://www.yelp.com/biz/cozy-cats-hotel-cary?osq=Pet+Boarding',
'https://www.yelp.com/biz/north-paw-animal-hospital-durham?osq=Pet+Boarding',
'https://www.yelp.com/biz/meowinn-morrisville?osq=Pet+Boarding',
'https://www.yelp.com/biz/amber-wright-pet-sitting-raleigh-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/kimies-kritters-hillsborough?osq=Pet+Boarding',
'https://www.yelp.com/biz/pets-companion-inn-durham-bahama?osq=Pet+Boarding',
'https://www.yelp.com/biz/k9-r-and-r-pet-retreat-rougemont-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/all-critters-petcare-raleigh?osq=Pet+Boarding',
'https://www.yelp.com/biz/paws-claws-and-hooves-chapel-hill-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/bone-voyage-pet-resort-garner?osq=Pet+Boarding',
'https://www.yelp.com/biz/pet-care-by-candace-raleigh?osq=Pet+Boarding'
)
for company in companys:
	time.sleep(2)
	driver = webdriver.Chrome(options=options, executable_path='/home/practice_environment/chromedriver')
	driver.get(company)
	time.sleep(4)

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
		features = 'N/A'
	col9.append(features)
	#row = f"Title: {title};,website: {website};,phone: {phone};,address: {address};,city_state: {city_state};,owner: {owner};,rating: {rating};,rating_count: {rating_count};,features: {features}"
	#rows.append(row)
	print(f"Completed: {title}")
	driver.quit()
	
#for data in rows:
#    print(data)
    
data = {'title':  col1,
        'website': col2,
        'phone': col3,
        'address': col4,
        'city_state': col5,
        'owner': col6,
        'rating': col7,
        'rating_count': col8,
        'features': col9
        }

df = pd.DataFrame (data, columns = ['title','website','phone','address','city_state','owner','rating','rating_count','features'])
df.to_csv (r'export_yelp_data.csv', index = False, header=True)

print (df)
