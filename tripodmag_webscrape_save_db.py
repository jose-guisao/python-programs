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


f = open("c:/Users/admin/OneDrive/Documents/python-programs/images/oftheMostBeautifulBeachesintheWorldTripOnMag_30Jan2022-2333", "r")

bs_obj_all = BSoup(f.read(),'html.parser')
db_name = "c:/Users/admin/OneDrive/Documents/python-programs/images/oftheMostBeautifulBeachesintheWorldTripOnMag_30Jan2022-2333" + '.db'
names  = []
links  = []
p_txts = []

# Selector tps_slideContainer_217 select container with h2,img/src,and p tags  

for i in bs_obj_all.select('#tps_slideContainer_217 > div'):
  name = i.h2.text
  names.append(name)
  image = i.figure.img['src']
  download_file(image)
  links.append(image)
  text = i.p.text
  p_txts.append(text)
  print(name)

db = sqlite3.connect(db_name)
cursor = db.cursor()
cursor.executescript('drop table if exists imgs_links;')
cursor.execute('''CREATE TABLE imgs_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT, content TEXT)''')
db.commit()

for i in range(0, len(links)):
  cursor.execute('''INSERT INTO imgs_links (id, link, name, content) VALUES (?,?,?,?)''',(i+1, links[i], names[i], p_txts[i]))
  print(i)
print("End second part ... saving database")
db.commit()
db.close()
f.close()
