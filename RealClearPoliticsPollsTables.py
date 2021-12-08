#Este programa trata de sacar los polls de general elections
#de Realclearpolitics y los guarda en un database
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup as BSoup
import os
from datetime import datetime
import time
import pandas as pd
import sqlite3
chromedriver = "H:/Downloads2/chromedriver/chromedriver.exe"
desired_capabilities=DesiredCapabilities.CHROME
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver,desired_capabilities=desired_capabilities)

url = 'https://www.realclearpolitics.com/epolls/latest_polls/general_election/'

driver.get(url)
bs_obj = BSoup(driver.page_source, 'html.parser')

start = datetime.now()
print(start)
title = driver.title # get page title
print(title)

driver.close()
driver.quit()

db = sqlite3.connect('pollsData.sqlite')
cursor = db.cursor()
cursor.executescript('drop table if exists polls;')
cursor.execute('''CREATE TABLE polls (id INT PRIMARY KEY NOT NULL, Date TEXT NOT NULL, Race TEXT NOT NULL, Poll TEXT NOT NULL, Results TEXT NOT NULL, Spread TEXT NOT NULL);''')

tables = bs_obj.findAll('table')
tr = bs_obj.findAll('tr')
td = bs_obj.findAll('td')
pollDate = bs_obj.findAll('b')

races = bs_obj.find_all("td", class_="lp-race")
polls = bs_obj.find_all("td", class_="lp-poll")
results = bs_obj.find_all("td", class_="lp-results")
spread = bs_obj.find_all("td", class_="lp-spread")

print("Total of polls :",len(races))
idx=0
for t in range(len(tables)):
    if len(tables[t].findAll('tr')) == 1:
        Date = tables[t].find('td').text
        continue
    for i in range(1,len(tables[t].findAll('tr'))):
        cursor.execute('''INSERT INTO polls (id, Date, Race, Poll, Results, Spread) VALUES (?,?,?,?,?,?)''',(idx+1,Date,races[idx].text,polls[idx].text,results[idx].text,spread[idx].text))
##        print(Date, '{:<5}'.format(races[idx].text),'{:<5}'.format(polls[idx].text),'{:<5}'.format(results[idx].text),'{:<5}'.format(spread[idx].text))
        idx = idx+1
##print(idx)
finish = datetime.now() - start
print(finish)
db.commit()
db.close()

print("END")

