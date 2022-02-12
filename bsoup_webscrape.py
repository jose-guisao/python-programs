from datetime import datetime
from bs4 import BeautifulSoup as BSoup
import requests, sqlite3, time, re

url = 'https://investingfuel.com/entertainment/27-stars-from-the-90s-where-are-they-now/'
url1 = ''
fname_stamp = datetime.now().strftime("_%d%b%Y-%H%M")

response = requests.get(url)
bs_obj = BSoup(response.content,'html.parser')
fname = bs_obj.title
# # removing special characters from a list of items in python
fname = ([re.sub('[^a-zA-Z]+', '', _) for _ in fname])
print(fname, fname_stamp)
f = open("c:/Users/admin/OneDrive/Documents/python-programs/images/" + ''.join(fname)+fname_stamp, "w")
db_name = "c:/Users/admin/OneDrive/Documents/python-programs/images/" +''.join(fname) + '.db'
names  = []
links  = []
p_txts = []

response = requests.get(url)
for page in range(1,156):
    bs_obj = BSoup(response.content,'html.parser')
##    print(url + str(page))
    name = bs_obj.find('h2').text
    names.append(name)
    print(name)
    link = bs_obj.find('figure').img['src']
    links.append(link)
##    print(link)
    p_txt = bs_obj.find('p').text
    p_txts.append(p_txt)
##    print(p_txt)
    time.sleep(1)
    response = requests.get(url + str(page))
    f.write(link + '\n')
##    response = requests.get(url + str(page))
    
'''
page_num = input('Enter start number: ')
for page in range(1, int(page_num)):
    url_dt = url + link_dt + str(d)
    response = requests.get(url_dt)
    time.sleep(1)
    bs_obj = BSoup(response.content, 'html.parser')
    toon_date = bs_obj.find('span', class_='toon-date').text
    dt1 = datetime.strptime(toon_date, '%A, %B %d, %Y')
    print('http:' + bs_obj.find('img', class_='cartoon-image')
          ['src'], ' ', toon_date)
    print(bs_obj.find('h4', class_='cartoon-author').a.text)
print('End program')
'''

db = sqlite3.connect(db_name)
cursor = db.cursor()
cursor.executescript('drop table if exists imgs_links;')
cursor.execute('''
    CREATE TABLE imgs_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT, content TEXT)
''')
db.commit()

for i in range(0, len(links)):
    cursor.execute('''INSERT INTO imgs_links (id, link, name, content) VALUES (?,?,?,?)''',(i+1, links[i], names[i], p_txts[i]))
print("End second part ... saving database")
db.commit()
db.close()
f.close()
