# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
# specify the url
# In this the url has the search for the item you looking
urlpage = 'https://groceries.asda.com/search/yogurt'
chromedriver = "C:/Users/admin/Downloads/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
print(urlpage)
# chromedriver = "C:/Users/admin/Downloads/chromedriver/chromedriver.exe"
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
#driver.quit()
# find elements by xpath
# results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
# print('Number of results', len(results))
results = driver.find_elements(By.XPATH,"//*[@id='main-content']/main/div[1]/div[4]/div/div[2]/ul")
print('Number of results', len(results))

# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product" : product_name, "link" : product_link})

# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)
