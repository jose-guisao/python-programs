# TopBoxOffice-New.py
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service

s = Service("C:/Users/admin/OneDrive/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)


def get_movies():
    url = 'https://www.rottentomatoes.com/browse/in-theaters/'
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    movies = driver.find_element(By.CLASS_NAME, 'div.mb-movie')
    # .mb-movies
# content-column > div:nth-child(5) > div.mb-movies
    # movies = driver.find_elements_by_xpath('//div[@class="mb-movies"]')
    # movies = driver.find_elements_by_xpath('//*[@id="content-column"]/div[2]/div[2]')
    moviesTop = []

    # print(movie)//*[@id="content-column"]/div[2]/div[2]
    for line in movies:
        #  #movies container
        name = driver.find_element_by_xpath(
            '//*[@class="mb-movie"]').text
        moviesTop.append([name])
    driver.quit()
    return moviesTop


if __name__ == '__main__':
    start = datetime.now()
    top_Movies = get_movies()
    finish = datetime.now() - start

    for movie in top_Movies:
        print(movie)
    print(finish)
