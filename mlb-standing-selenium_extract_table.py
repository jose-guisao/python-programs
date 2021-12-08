import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

#path = 'chromedriver'
#driver = webdriver.Chrome(path)
driver = webdriver.Chrome(executable_path=r'C:/Users/jguisao/Downloads/chromedriver_win32/chromedriver.exe')

url = 'https://www.mlb.com/standings'

driver.get(url)
#time.sleep(10)

#//*[@id='regularSeason-division-201']/div/div/div[1]/div/table/thead/tr/th[1]

row_count = len(driver.find_elements_by_xpath("//*[@id='regularSeason-division-201']/div/div/div[1]/div/table/tbody/tr"))
col_count = len(driver.find_elements_by_xpath("//*[@id='regularSeason-division-201']/div/div/div[1]/div/table/tbody/tr[1]/td"))

print("Number of Rows ", row_count)
print("Number of Columns ", col_count)

first_part = "//*[@id='regularSeason-division-201']/div/div/div[1]/div/table/thead/tr/th["
second_part = "]"
table= []

for n in range(1, col_count+1):
    final_path = first_part+str(n)+second_part
    table_data = driver.find_element_by_xpath(final_path).text.replace('\n', ' ')
    table.append(table_data)
    #print(table[n-1])
print(table, end = " ")
print("")



first_part = "//*[@id='regularSeason-division-201']/div/div/div[1]/div/table/tbody/tr["
second_part = "]"
third_part = "]"
table= []
for n in range(1, row_count+1):
    #for m in range(1,col_count+1):
    #    final_path = first_part+str(n)+second_part+str(m)+third_part
    final_path = first_part+str(n)+second_part
    table_data = driver.find_element_by_xpath(final_path).text.replace('\n', ' ')
    table.append(table_data)
    print(table[n-1])
    #print(table_data, end = " ")
    #print("")

#driver.close()
