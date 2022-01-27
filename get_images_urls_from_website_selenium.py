# Este codigo trabaja --> elimina los popups
# falta verificar cuantas fotos/img hay en el post
#https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=findNextSiblings#searching-the-tree

from bs4 import BeautifulSoup as BSoup
##from urllib.request import Request, urlopen
from selenium import webdriver
import requests, datetime, sqlite3, re, time
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

url0 = 'https://stacker.com/stories/1134/50-best-movies-60s'
url1 = 'https://stacker.com/stories/1173/50-celebrities-you-might-not-know-are-lgtbq'
url2 = 'https://stacker.com/stories/959/50-best-college-movies'
url3 = 'https://stacker.com/stories/946/100-best-john-wayne-movies'
url4 = 'https://stacker.com/stories/2410/best-black-and-white-films-all-time'
url5 = 'https://stacker.com/stories/3346/50-best-space-movies-all-time'
url6 = 'https://stacker.com/stories/3362/30-best-nature-documentaries-all-time'
response = requests.get(url6)
bs_obj = BSoup(response.text, 'html.parser')

fname_stamp = datetime.datetime.now().strftime("_%d%b%Y-%H%M")

#use page title for db name and file name
fname = bs_obj.title
# # removing special characters from a list of items in python
fname = ([re.sub('[^a-zA-Z]+', '', _) for _ in fname])
print(fname,fname_stamp)
#convert list to string

f = open("c:/Users/admin/OneDrive/Documents/python-programs/images/"+''.join(fname)+fname_stamp, "w")
db_name = ''.join(fname) + '.db'
photos = [] # list to save links
names = []
contents = []
# Select container that have all the images and articles
container_pics = bs_obj.select_one('#block-stacker-content > article > div.ct-slideshow__slides')

for pic in container_pics.find_all('img'):
        f.write(str(pic['src'])+'\n')
        print(str(pic['src'])+'\n')
        photos.append(pic['src'])
        time.sleep(1)
        download_file(pic['src']) # download file and save it
f.close()

for name in container_pics.findAll('h2'):
##	print(name.text)
	names.append(name.text)

for content in container_pics.findAll('p'):
##        print(content.text)
        contents.append(content.text)
	

print("End first part...")

db = sqlite3.connect(db_name)
cursor = db.cursor()
cursor.executescript('drop table if exists img_links;')
cursor.execute('''
    CREATE TABLE img_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT,
                       content TEXT)
''')
db.commit()

for i in range(1,len(photos)):
        cursor.execute('''INSERT INTO img_links (id, link, name, content) VALUES (?,?,?,?)''',(i+1,photos[i],names[i],contents[i]))
print("End second part ... saving database")
db.commit()
db.close()
##driver.close()
##driver.quit()
