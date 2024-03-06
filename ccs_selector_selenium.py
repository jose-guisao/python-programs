from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
chromedriver = "e:/Downloads2/chromedriver/chromedriver.exe"
desired_capabilities=DesiredCapabilities.CHROME
driver = webdriver.Chrome(chromedriver)
##driver = webdriver.Chrome(chromedriver,desired_capabilities=desired_capabilities)
#url = "http://udemycoupon.discountsglobal.com/coupon-category/free-2/" este url no funciona va a bedbath and beyond 
url = "https://www.udemy.com/courses/development/data-science/"

driver.get(url)
#elems = driver.find_elements_by_css_selector('[id*=\"coupon-link\"]') # este selector no funciona
elems = driver.find_elements_by_css_selector('[id*="course-unit-container-Mspopulares"]')
css_lnks = [i.get_attribute('href') for i in driver.find_elements_by_css_selector('[id*=coupon-link]')]
xpth_lnks = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//a[contains(@id,'coupon-link-')]")]

for lnk in xpth_lnks:
    print(lnk)

for lnk in css_lnks:
    print(lnk)
##print(css_lnks)
##print(elems)

#u135-tabs--759-content-0
