#Esta version usa un metodo mas rapido ...
#Este programa trata de sacar los polls de general elections de Realclearpolitics
#Este codigo tiene los primeros intentos de usar selenium
import urllib.request
from bs4 import BeautifulSoup as BSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
from datetime import datetime
import pandas as pd
import sqlite3


db = sqlite3.connect('pollsDataBase.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE polls(id INTEGER PRIMARY KEY, Date TEXT, Race_Topic TEXT,
                       Poll TEXT, Results TEXT, Spread TEXT)
''')

db.commit()


##path = 'chromedriver'
##driver = webdriver.Chrome(path)
chromedriver = "C:/Users/jguis/Downloads/chromedriver/chromedriver.exe"
desired_capabilities=DesiredCapabilities.CHROME
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver,desired_capabilities=desired_capabilities)

url = 'https://www.realclearpolitics.com/epolls/latest_polls/general_election/'

driver.get(url)
bs_obj = BSoup(driver.page_source, 'html.parser')
start = datetime.now()
title = bs_obj.title.text
my_nav = driver.find_elements_by_xpath("//*[@id='my-nav']//*[contains(@id,'link')]")
num_of_pages = len(my_nav) # find how may links to move page

print("Numero de links/paginas: ",num_of_pages)

driver.implicitly_wait(15)
alert = driver.switch_to.active_element
handle=driver.window_handles
alert = driver.switch_to.window(handle[0])
alert = driver.switch_to.active_element
container_tables = driver.find_elements_by_xpath("//*[@id='container']//*[contains(@id,'table')]")

time.sleep(5)

table_count = len(bs_obj.findAll('table'))
#para verificar la cantidad de tablas
#Verificar cuantas lineas(rows) hay y cuantas columnas

row_count_per_table = len(driver.find_elements_by_xpath("//*[@id='table-1']/table[1]/tbody/tr"))
rows_total = len(bs_obj.findAll('tr'))
col_no = len(bs_obj.find('thead').findAll('th'))
                  
tag = bs_obj.findAll('b')

tables = bs_obj.findAll('table', attrs={'class':'sortable'}) # todas las tablas



l=[]
data = ''
for i in range(len(tables)):
    table_rows = tables[i].findAll('tr')
    for tr in table_rows:
        td = tr.findAll('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        
print("end loop")


finish = datetime.now() - start 
driver.quit()
