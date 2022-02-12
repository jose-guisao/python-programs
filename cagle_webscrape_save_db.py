from bs4 import BeautifulSoup as BSoup

import sqlite3, requests


def download_file(url):
    local_fname = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("c:/Users/admin/OneDrive/Documents/python-programs/images/"+local_fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_fname


with open("c:/Users/admin/OneDrive/Documents/python-programs/images/cagle/Cartoonists_06Feb2022-2207", "r",encoding="utf-8") as f:
    bs_obj_all = BSoup(f.read(),'html.parser')

db_name = "c:/Users/admin/OneDrive/Documents/python-programs/images/cagle/Cartoonists_06Feb2022-2207" + '.db'
captions  = []
links  = []
authors = []

##print(bs_obj_all.prettify())
## Selector tps_slideContainer_217 select container with h2,img/src,and p tags  
##for i in range(0,len(bs_obj_all.findAll('div',class_='media'))):
##    print(bs_obj_all.findAll('div',class_='media')[i].a.text)
##images = ['http:' + i.img['src'] for i in bs_obj_all.findAll('article')]

pags_titles = bs_obj_all.findAll('title')
for x in pags_titles:
    print(x.text.strip())

try:
    for x in bs_obj_all.findAll('article'):
        link = x.find('div',class_='media').findNext('a').text.strip()
        captions.append(link)
    ##    link = x.find('div',class_='media').findNext('a')['href']
        image = 'http:' + x.find('div',class_='media').findNext('img')['src']
        links.append(image)
        author = x.find('span',class_='post-author-link').a.text.strip()
        authors.append(author)
        print(link,image,author)
except AttributeError:
    print('Error NoneType Not Found')
    
print('End of program')

##  name = i.h2.text
##  names.append(name)
##  image = i.figure.img['src']
##  download_file(image)
##  links.append(image)
##  text = i.p.text
##  p_txts.append(text)
##  print(name)

db = sqlite3.connect(db_name)
cursor = db.cursor()
cursor.executescript('drop table if exists imgs_links;')
cursor.execute('''CREATE TABLE imgs_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT, content TEXT)''')
db.commit()

for i in range(0, len(links)):
  cursor.execute('''INSERT INTO imgs_links (id, link, name, content) VALUES (?,?,?,?)''',(i+1, captions[i], links[i], authors[i]))

print("End second part ... saving database")
db.commit()
db.close()
