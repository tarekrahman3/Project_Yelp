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
options.add_argument('--ignore-certificate-errors')
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
'https://www.yelp.com/biz/a-pets-life-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/d-tails-pet-grooming-augusta-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/elite-pet-service-of-augusta-augusta-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/hill-high-animal-hospital-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/barking-lot-boutique-evans-8?osq=Pet+Boarding',
'https://www.yelp.com/biz/paws-in-paradise-resort-and-spa-evans?osq=Pet+Boarding',
'https://www.yelp.com/biz/animal-house-augusta-5?osq=Pet+Boarding',
'https://www.yelp.com/biz/starlings-camp-canine-appling?osq=Pet+Boarding',
'https://www.yelp.com/biz/springwood-pet-boarding-and-grooming-hephzibah-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/st-francis-animal-hospital-augusta-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/paradise-animal-hospital-augusta-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/all-gods-creatures-veterinary-hospital-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/blue-willow-pet-and-home-services-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/dawg-tired-augusta-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/paradise-kennels-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/animal-boutique-martinez-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/pawwd-pets-are-what-we-do-grovetown-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/a-pets-and-plants-evans-4?osq=Pet+Boarding',
'https://www.yelp.com/biz/highland-animal-hospital-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/acute-care-veterinary-clinic-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/ol-red-kennels-waynesboro?osq=Pet+Boarding',
'https://www.yelp.com/biz/head-to-tail-small-dog-groom-and-board-warrenville?osq=Pet+Boarding',
'https://www.yelp.com/biz/denegar-kennels-and-pet-pickup-service-aiken-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/the-animal-house-augusta-4?osq=Pet+Boarding',
'https://www.yelp.com/biz/the-dog-mom-evans-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/floyds-good-dog-kennels-grovetown?osq=Pet+Boarding',
'https://www.yelp.com/biz/boarding-and-grooming-at-ivy-falls-grovetown?osq=Pet+Boarding',
'https://www.yelp.com/biz/north-augusta-animal-hospital-north-augusta?osq=Pet+Boarding',
'https://www.yelp.com/biz/tender-love-and-pet-care-columbus-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/rockstar-paws-pet-grooming-and-boarding-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/northridge-veterinary-center-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/2nd-home-pet-resort-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/northside-animal-hospital-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/yuppy-puppy-grooming-and-boarding-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/paws-kountry-smiths-station?osq=Pet+Boarding',
'https://www.yelp.com/biz/2nd-avenue-animal-hospital-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/lee-lees-world-columbus-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/dog-gone-good-dog-training-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/pups-at-tiffanys-as-the-dog-house-columbus?osq=Pet+Boarding',
'https://www.yelp.com/biz/companion-animal-hospital-phenix-city?osq=Pet+Boarding',
'https://www.yelp.com/biz/northridge-veterinary-center-columbus-3?osq=Pet+Boarding',
'https://www.yelp.com/biz/the-dog-coach-opelika?osq=Pet+Boarding',
'https://www.yelp.com/biz/smiths-station-animal-hospital-smiths-station-2?osq=Pet+Boarding',
'https://www.yelp.com/biz/pawsitively-purrfect-grooming-salon-and-pet-spa-valley?osq=Pet+Boarding'
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
	print(f"Completed: {title}")
	driver.quit()
   
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
df.to_csv (r'export_yelp_lastbatch.csv', index = False, header=True)

print (df)
