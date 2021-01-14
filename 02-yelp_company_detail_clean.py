from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")

rows = []
companys = (
'https://www.yelp.com/biz/home-sweet-home-pet-sitting-greensboro-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/best-friends-bed-and-biscuit-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/petsuites-greensboro-greensboro-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/purr-life-luxury-cat-resort-and-grooming-greensboro-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/andreas-go-fetch-pet-sitting-greensboro-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/rhonda-triad-pet-sitter-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/animal-ark-of-brassfield-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/west-market-veterinary-hospital-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/pets-u-love-greensboro-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/oak-ridge-animal-hospital-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/cat-care-hospital-greensboro-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/southwoods-animal-hospital-greensboro-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/gate-city-animal-hospital-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/cat-clinic-of-greensboro-greensboro-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/university-animal-hospital-of-greensboro-greensboro-4?osq=Pet+Boarding',
'https://www.yelp.com/biz/bel-aire-veterinary-hospital-greensboro-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/almost-home-boarding-and-grooming-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/pet-sitting-plus-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/benessere-animal-hospital-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/rodger-w-kleisch-dvm-forest-oaks-animal-hospital-greensboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/phoenix-animal-hospital-gibsonville?osq=Pet+Boarding',
'https://www.yelp.com/biz/kims-backyard-and-barnyard-pet-and-critter-care-kernersville?osq=Pet+Boarding',
'https://www.yelp.com/biz/hill-clark-farm-siler-city?osq=Pet+Boarding',
'https://www.yelp.com/biz/james-landing-veterinary-hospital-jamestown?osq=Pet+Boarding',
'https://www.yelp.com/biz/high-point-veterinary-hospital-high-point?osq=Pet+Boarding',
'https://www.yelp.com/biz/skeet-club-veterinary-hospital-high-point?osq=Pet+Boarding',
'https://www.yelp.com/biz/the-animal-hospital-at-lake-brandt-summerfield?osq=Pet+Boarding',
'https://www.yelp.com/biz/westchester-veterinary-hospital-high-point?osq=Pet+Boarding',
'https://www.yelp.com/biz/professional-paws-academy-kernersville?osq=Pet+Boarding',
'https://www.yelp.com/biz/winston-veterinary-hospital-winston-salem?osq=Pet+Boarding',
'https://www.yelp.com/biz/the-prominent-dog-training-academy-burlington?osq=Pet+Boarding',
'https://www.yelp.com/biz/northwood-animal-hospital-high-point?osq=Pet+Boarding',
'https://www.yelp.com/biz/northwest-animal-hospital-oak-ridge?osq=Pet+Boarding',
'https://www.yelp.com/biz/balance-vet-hospital-kernersville?osq=Pet+Boarding'
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
	try:
		website = driver.find_element_by_xpath('//section[1]/div/div[1]/div/div[1]/p[2]/a').text
	except:
		try:
		        website = driver.find_element_by_xpath('//section[2]/div/div[1]/div/div[1]/p[2]/a').text
		except:
		        website = 'N/A'
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
	try:
		address = driver.find_element_by_xpath('//address/p').text
	except:
		address = 'N/A'
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
	try:
		rating = driver.find_element_by_xpath('//div/div/div[2]/div[1]/span/div').get_attribute('aria-label')
	except:
		rating = 'N/A'
	try:
		rating_count = driver.find_element_by_xpath('//div/div/div[2]/div[2]/span').text
	except:
		rating_count = 'N/A'
	try:
		features = driver.find_element_by_xpath('//div/div[3]/div[1]/div[1]/div/div/span[2]').text
	except:
		features = 'N/A'
	row = f"Title: {title};,website: {website};,phone: {phone};,address: {address};,city_state: {city_state};,owner: {owner};,rating: {rating};,rating_count: {rating_count};,features: {features}"
	rows.append(row)
	print(f"Completed: {title}")
	driver.quit()
	
for data in rows:
    print(data)
