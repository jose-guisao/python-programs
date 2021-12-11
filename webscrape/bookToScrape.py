#From article: https://www.scrapingdog.com/blog/best-python-web-scraping-libraries
from typing import Container
from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://books.toscrape.com/'
driver = webdriver.Chrome('E:\Downloads2\chromedriver\chromedriver.exe')
driver.get(url)
container = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol')
# get book titles
titles = container.find_elements(By.TAG_NAME,'a')
for title in titles:
    print(title.text)

driver.close()

# //*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a
# //*[@id="default"]/div/div/div/div/section/div[2]/ol
# //*[@id="default"]/div/div/div/div/section/div[2]/div/ul/li[2]/a