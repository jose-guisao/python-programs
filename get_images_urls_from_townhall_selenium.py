# Este codigo trabaja --> elimina los popups
# falta verificar cuantas fotos/img hay en el post
# https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=findNextSiblings#searching-the-tree

from bs4 import BeautifulSoup as BSoup
##from urllib.request import Request, urlopen
from selenium import webdriver
import requests
import datetime
import sqlite3
import re
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#ser = Service("C:\\chromedriver.exe")


urls = [
    'https://stacker.com/stories/1134/50-best-movies-60s',
    'https://stacker.com/stories/1173/50-celebrities-you-might-not-know-are-lgtbq',
    'https://stacker.com/stories/959/50-best-college-movies',
    'https://stacker.com/stories/946/100-best-john-wayne-movies',
    'https://stacker.com/stories/2410/best-black-and-white-films-all-time',
    'https://stacker.com/stories/3346/50-best-space-movies-all-time',
    'https://stacker.com/stories/3362/30-best-nature-documentaries-all-time',
    'https://stacker.com/stories/2189/50-best-colleges-east-coast',
    'https://stacker.com/stories/145/top-100-country-songs-all-time',
    'https://stacker.com/stories/980/100-best-tv-shows-all-time']
# https://townhall.com/political-cartoons/patcross/2022/01/12/187713
url = 'https://townhall.com/political-cartoons'

ser = Service('C:/Users/admin/OneDrive/chromedriver/chromedriver.exe')
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

##driver = webdriver.Chrome(chromedriver)
s.get(url)


def download_file(url):
    local_fname = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("c:/Users/admin/OneDrive/Documents/python-programs/images/"+local_fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_fname


response = requests.get(url)
bs_obj = BSoup(s.page_source, 'html.parser')
fname_stamp = datetime.datetime.now().strftime("_%d%b%Y-%H%M")
# use page title for db name and file name
fname = bs_obj.title
# # removing special characters from a list of items in python
fname = ([re.sub('[^a-zA-Z]+', '', _) for _ in fname])
print(fname, fname_stamp)
f = open("c:/Users/admin/OneDrive/Documents/python-programs/images/" +
         ''.join(fname)+fname_stamp, "w")
db_name = "c:/Users/admin/OneDrive/Documents/python-programs/images/" + \
    ''.join(fname) + '.db'

toons_lnks = []  # list to save links
authors = []
dates = []

chk_date = True

while chk_date == True:
    f.write(bs_obj.find('img', class_='cartoon-image')['src']+'\n')
    author = bs_obj.find('h4', class_='cartoon-author').a.text
    btn_forward = s.find_element(
        By.XPATH, "//*[@id='slideshow-container']/div[1]/div[1]/div[1]/a/i").click()
    bs_obj = BSoup(s.page_source, 'html.parser')
    time.sleep(1)
    toon_date = s.find_element(
        By.XPATH, "//*[@id='slideshow-container']/div[1]/div[2]/h4/span")
    toons_lnks.append(bs_obj.find('img', class_='cartoon-image')['src']+'\n')
    authors.append(author)
    dates.append(toon_date.text)
    print(toon_date.text)
    print(bs_obj.find('img', class_='cartoon-image')['src'])
    if 'November 24' in s.find_element(By.XPATH, "//*[@id='slideshow-container']/div[1]/div[2]/h4/span").text:
        chk_date = False
        print('Reach end')
    else:
        chk_date = True
f.close()
db = sqlite3.connect(db_name)
cursor = db.cursor()
cursor.executescript('drop table if exists img_links;')
cursor.execute('''
    CREATE TABLE toon_img_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT, content TEXT)
''')
db.commit()

for i in range(0, len(toons_lnks)):
    cursor.execute('''INSERT INTO toon_img_links (id, link, name, content) VALUES (?,?,?,?)''',
                   (i+1, toons_lnks[i], authors[i], dates[i]))
print("End second part ... saving database")
db.commit()
db.close()
s.close()
s.quit()
