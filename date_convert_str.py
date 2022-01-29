from datetime import datetime
from bs4 import BeautifulSoup as BSoup
import requests
import sqlite3
import time
url = 'https://townhall.com/political-cartoons'
url1 = 'https://townhall.com/political-cartoons/2022/01/27'
day = input('Enter day number: ')
link_dt = '/2022/01/'
for d in range(1, int(day)):
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
