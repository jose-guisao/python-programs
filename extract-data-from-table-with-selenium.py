#https://stackoverflow.com/questions/50914072/extracting-data-from-a-table-in-html-using-selenium-and-python
from selenium import webdriver
import time 
import pandas as pd
import urllib.request
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

chromedriver = "C:/Users/jguis/Downloads/chromedriver/chromedriver.exe"
desired_capabilities=DesiredCapabilities.CHROME
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver,desired_capabilities=desired_capabilities)

url = 'https://www.bseindia.com/corporates/ann.aspx?expandable=0'
#url = 'https://www.bseindia.com/corporates/ann.html'

driver.get(url)

time.sleep(5) # wait 5 seconds until DOM will load completly
table = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblann"]/table/tbody')

for row in table.find_elements_by_xpath('./tr'):
    print(row.text)
