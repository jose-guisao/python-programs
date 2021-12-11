# https://medium.com/@winston.smith.spb/python-selenium-speed-scraping-45bda525e42
# Python: Selenium Speed Scraping

from datetime import datetime
from selenium import webdriver
chromedriver = "H:/Downloads2/chromedriver/chromedriver.exe"


def get_states():
    url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)

    rows = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody')\
        .find_elements_by_tag_name('tr')

    states = []

    for row in rows:
        cells = row.find_elements_by_tag_name('td')
        name = row.find_element_by_tag_name('th').text
        abbr = cells[0].text
        established = cells[-9].text
        population = cells[-8].text
        total_area_km = cells[-6].text
        land_area_km = cells[-4].text
        water_area_km = cells[-2].text

        states.append([
            name, abbr, established, population, total_area_km, land_area_km,
            water_area_km
        ])
    driver.quit()
    return states


if __name__ == '__main__':
    start = datetime.now()
    states = get_states()
    finish = datetime.now() - start
    print(states)
    print(finish)
