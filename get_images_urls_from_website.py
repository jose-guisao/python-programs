# Este codigo trabaja --> elimina los popups
# falta verificar cuantas fotos/img hay en el post
#https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=findNextSiblings#searching-the-tree

from bs4 import BeautifulSoup as BSoup
##from urllib.request import Request, urlopen
from selenium import webdriver
import requests, time, sqlite3, re
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException

##chromedriver = 'C:/Users/admin/OneDrive/chromedriver/chromedriver.exe'
##driver = webdriver.Chrome(chromedriver)
##driver.get(url)

def download_file(url):
    local_fname = url.split('/')[-1]
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open("c:/Users/admin/OneDrive/Documents/python-programs/images/"+local_fname, 'wb') as f:
                  for chunk in r.iter_content(chunk_size=8192):
                      f.write(chunk)
    return local_fname

url = 'https://stacker.com/stories/1173/50-celebrities-you-might-not-know-are-lgtbq'
response = requests.get(url)
bs_obj = BSoup(response.text, 'html.parser')

#use page title for db name and file name
fname = bs_obj.title
# # removing special characters from a list of items in python
fname = ([re.sub('[^a-zA-Z0-9]+', '', _) for _ in fname])
print(fname)
#convert list to string
f = open("c:/Users/admin/OneDrive/Documents/python-programs/"+''.join(fname), "w")
db_name = ''.join(fname) + '.db'
photos = [] # list to save links
names = []
contents = []
# Select container that have all the images and articles
container_pics = bs_obj.select_one('#block-stacker-content > article > div.ct-slideshow__slides')

for pic in container_pics.find_all('img'):
	f.write(str(pic['src'])+'\n')
	photos.append(pic['src'])
	time.sleep(2)
	download_file(pic['src'])
f.close()

for name in container_pics.findAll('h2'):
	print(name.text)
	names.append(name.text)

for content in container_pics.findAll('p'):
        print(content.text)
        contents.append(content.text)
	
##pictures = bs_obj.findAll('picture')

##    print(i,name)
##    for img in imgs_links:
##        photos.append(img["src"])
print("End first part...")

db = sqlite3.connect(db_name)
cursor = db.cursor()
cursor.executescript('drop table if exists img_links;')
cursor.execute('''
    CREATE TABLE img_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT,
                       content TEXT)
''')
db.commit()
idx = 0
for i in range(1,len(photos)):
        cursor.execute('''INSERT INTO img_links (id, link, name, content) VALUES (?,?,?,?)''',(i+1,photos[i],names[i],contents[i]))
        idx=idx+1
print("End second part ... saving database")
db.commit()
db.close()
##driver.close()
##driver.quit()
