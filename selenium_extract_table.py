import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

#path = 'chromedriver'
#driver = webdriver.Chrome(path)
driver = webdriver.Chrome(
    executable_path=r'C:/Users/admin/OneDrive/chromedriver/chromedriver.exe')

url = 'https://infobypokharelk.blogspot.com'

driver.get(url)

row_count = len(driver.find_elements_by_xpath(
    "//*[@id='post-body-6767393087210111064']/div[1]/table/tbody/tr"))
col_count = len(driver.find_elements_by_xpath(
    "//*[@id='post-body-6767393087210111064']/div[1]/table/tbody/tr[1]/td"))
print("Number of Rows ", row_count)
print("Number of Columns ", col_count)

first_part = "//*[@id='post-body-6767393087210111064']/div[1]/table/tbody/tr["
second_part = "]/td["
third_part = "]"
for n in range(1, row_count+1):
    for m in range(1, col_count+1):
        final_path = first_part+str(n)+second_part+str(m)+third_part
        table_data = driver.find_element_by_xpath(final_path).text
        print(table_data, end=" ")
    print("")
