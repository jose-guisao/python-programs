# Este codigo trabaja --> elimina los popups
# falta verificar cuantas fotos/img hay en el post
# https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=findNextSiblings#searching-the-tree

from bs4 import BeautifulSoup as BSoup
from selenium import webdriver
import requests, datetime, sqlite3, re, time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException


def download_file(url):
    local_fname = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("c:/Users/admin/OneDrive/Documents/python-programs/images/"+local_fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_fname


def web_scrape(url):
    response = requests.get(url)
    bs_obj = BSoup(response.text, 'html.parser')
    fname_stamp = datetime.datetime.now().strftime("_%d%b%Y-%H%M")
    # use page title for db name and file name
    fname = bs_obj.title
    #print(fname) ## DEBUG   
    # # removing special characters from a list of items in python
    fname = ([re.sub('[^a-zA-Z]+', '', _) for _ in fname])
    #nombre_de_archivo = ''.join(fname) # convert list to string
    print(fname[0]+fname_stamp) #debugging
    # convert list to string
    ## ESTE DIRECTORIO c:/Users/admin/OneDrive/Documents/python-programs/images/ no existe en esta PC
    ## y da error, tuve que cambiarlo a jguis
    f = open(
        "c:/Users/jguis/OneDrive/Documents/python-programs/images/"+''.join(fname), "w")
    db_name = "c:/Users/jguis/OneDrive/Documents/python-programs/images/" + \
        ''.join(fname) + '.db'
    photos = []  # list to save links
    names = []
    contents = []
    # Select container that have all the images and articles
    container_pics = bs_obj.select_one(
        '#block-stacker-content > article > div.ct-slideshow__slides')
    for pic in container_pics.find_all('img'):
        f.write(str(pic['src'])+'\n')
        print(str(pic['src'])+'\n')
        photos.append(pic['src'])
        time.sleep(1)
##        download_file(pic['src']) # download file and save it
        print('call download file . . . .')
    f.close()

    for name in container_pics.findAll('h2'):
        # print(name.text)
        names.append(name.text)

    for content in container_pics.select('div.ct-slideshow__slide__text-container'):
    #for content in container_pics.findAll('p'):
        # print(content.text)
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

    for i in range(0, len(photos)):
        cursor.execute('''INSERT INTO img_links (id, link, name, content) VALUES (?,?,?,?)''',
                       (i+1, photos[i], names[i], contents[i]))
    print("End second part ... saving database")
    db.commit()
    db.close()


urlsx = [
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

urls = ['https://stacker.com/stories/1812/100-best-films-21st-century-according-critics']
urls0 = ['https://stacker.com/stories/3346/50-best-space-movies-all-time']
for url in range(0, len(urls)):
    print(url, urls[url])
    web_scrape(urls[url])
