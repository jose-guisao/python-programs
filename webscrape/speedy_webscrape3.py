# https://medium.com/@winston.smith.spb/python-selenium-speed-scraping-45bda525e42
# Python: Selenium Speed Scraping

from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup as BSoup
chromedriver = "H:/Downloads2/chromedriver/chromedriver.exe"


url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
url1 = 'https://www.realclearpolitics.com/epolls/latest_polls/general_election/'
driver = webdriver.Chrome(chromedriver)
driver.get(url)
start = datetime.now()
bs_obj = BSoup(driver.page_source, 'html.parser')
rows = bs_obj.find_all('table')[0].find('tbody').find_all('tr')
states = []
for row in rows:
    cells = row.find_all('td')
    name = row.find('th').get_text()
    abbr = cells[0].get_text()
    established = cells[-9].get_text()
    population = cells[-8].get_text()
    total_area_km = cells[-6].get_text()
    land_area_km = cells[-4].get_text()
    water_area_km = cells[-2].get_text()

    states.append([
        name, abbr, established, population, total_area_km, land_area_km,
        water_area_km
    ])


finish = datetime.now() - start
# print(states)
# print(finish)
