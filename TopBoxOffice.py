# import requests
# import urllib
# from bs4 import BeautifulSoup
# from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.rottentomatoes.com/browse/in-theaters/'

driver = webdriver.Chrome(
    executable_path=r'H:/Downloads2/chromedriver/chromedriver.exe')
driver.get(url)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# https://stackoverflow.com/questions/30002313/selenium-finding-elements-by-class-name-in-python
show_more = driver.find_element_by_xpath(
    "//BUTTON[@type='button'][text()='Show More']").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print("click on show more")
driver.implicitly_wait(15)
movieTBO = driver.find_element_by_xpath(
    "//DIV[@class='mb-movies']/self::DIV")
print(type(movieTBO))
print(movieTBO.text)

# movies = movieTBO.find_elements_by_class("mb-movie")
# for e in range(len(movies)):
#     print(e, movies[e].text)
# driver.close()
# print(len(elements))
