#Este codigo trabaja --> elimina los popups
# falta verificar cuantas fotos/img hay en el post
#
# import urllib.request
from bs4 import BeautifulSoup as BSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException
import sqlite3
import re

db = sqlite3.connect('ImagesLinksDataBase.db')
cursor = db.cursor()
cursor.executescript('drop table if exists img_links;')
cursor.execute('''
    CREATE TABLE img_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT,
                       content TEXT)
''')
db.commit()

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
# chromedriver = "C:/Users/jguis/Downloads/chromedriver/chromedriver.exe"
chromedriver = "C:/Users/jguis/Downloads/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(chromedriver,options=options)
url = 'http://readysethealth.com/20-celebrities-you-didnt-know-were-lgbtq/'
driver.get(url)
# req =  Request(url,headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
bs_obj = BSoup(driver.page_source, 'html.parser')

images = bs_obj.findAll('img')
i=0
# for image in images:
# i = i + 1
# print(i,image['src'])
##print(len(images))
##driver.close()
##driver.quit()

'''
//*[@id="post-15013"]/div/div[3]/a
for i in  elements:
    image = i.find_element_by_tag_name("img")
    img_src = image.get_attribute("src")
'''
photos=[]
names=[]
for i in range(1,5):
##    time.sleep(3)
# Move to next page
# Search for images links
    try:
        next_pag = driver.find_element_by_xpath("//*/div/div[3]/a")
        # next_pag = driver.find_element_by_xpath("//*[contains(text(), 'next page')]")
        next_pag.click()
        bs_obj = BSoup(driver.page_source, 'html.parser')
    except (ElementNotVisibleException, ElementClickInterceptedException) as exception:
        print("Element is no visible Message: element not interactable")
        popup_close = driver.find_element_by_xpath("//*[@id='revexitcloseme']")
        popup_close.click()
    name = bs_obj.find('h3').text
    names.append(name)
    time.sleep(5)
##    imgs_links = bs_obj.findAll('img')
    imgs_links = bs_obj.find_all('img', {'src':re.compile('.jpg')})
    imgs = driver.find_elements_by_xpath("//img[@src]")
    print(i,name)
    for img in imgs_links:
        photos.append(img["src"])
print("End first part...")
content=""

idx=0
for i in range(1,len(photos)):
        cursor.execute('''INSERT INTO img_links (id, link, name, content) VALUES (?,?,?,?)''',(idx+1,photos[i],names[i],content))
        idx=idx+1
print("End second part ... saving database")
db.commit()
db.close()
driver.close()
driver.quit()

