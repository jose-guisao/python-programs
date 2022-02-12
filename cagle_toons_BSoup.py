from datetime import datetime
from bs4 import BeautifulSoup as BSoup
import requests, sqlite3, time, re
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service('C:/Users/admin/OneDrive/chromedriver/chromedriver.exe')
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

def get_page_sel(url):
    s.get(url)
    time.sleep(4)
    s.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    bs_sel_obj = BSoup(s.page_source, 'html.parser')
    return bs_sel_obj.prettify()
    
def get_page(url):
    wait_time = randint(20,30)
    time.sleep(wait_time)
    response = requests.get(url)
    print(response.status_code, '',wait_time,' secs')
    time.sleep(4)
    bs_obj = BSoup(response.content,'html.parser')
    return bs_obj.prettify()

def get_cagle_cartoonists(url):
    urlstr = 'https://www.cagle.com/author/'
    response = requests.get(url)
#    if response.status_code == '200':
    bs_obj = BSoup(response.content,'html.parser')
    cartoonist_index = bs_obj.select('#dcpci-cartoonist-index')
    authors = [a.text for a in cartoonist_index[0].findAll('a')]
    names_list_url = [x.replace('.','') for x in authors]
    authors = [x.replace(' ','-') for x in names_list_url]
    names_list_url = [x for x in authors if x.strip()]
    names_url = [urlstr + str(x) + "/" for x in names_list_url]
    return names_url

url = 'https://www.cagle.com/cartoonists/'
fname_stamp = datetime.now().strftime("_%d%b%Y-%H%M")

response = requests.get(url)
bs_obj = BSoup(response.content,'html.parser')
fname = bs_obj.title
print(fname.text)
fname = ([re.sub('[^a-zA-Z]+', '', _) for _ in fname])

##print('the lenght of list is; ',len(get_cagle_cartoonists(url)))
##[print(x) for x in get_cagle_cartoonists(url)]
##
##results = [print(i, x) for i , x in enumerate(get_cagle_cartoonists(url))]

upper_limit = 0
lower_limit = 82
list_url = get_cagle_cartoonists(url)

##results = [print(i, x) for i , x in enumerate(names_url)]
##[print(x,'',list_url[x]) for x in range(0+len(list_url)-lower_limit,len(list_url)-upper_limit)]
print('lenght of list ',len(list_url))
print('lower limit ',len(list_url)-lower_limit)
print('upper limit ',len(list_url)-upper_limit)


##r = [print(x) for x in names_url]
print('Enter in for loop ... delay time is between 20 to 30 secs per request..')
for url in range(0+len(list_url)-lower_limit,len(list_url)-upper_limit):
    print(list_url[url])
    with open("c:/Users/admin/OneDrive/Documents/python-programs/images/cagle/" + ''.join(fname) + fname_stamp, "a", encoding="utf-8") as f:
        f.write(get_page(list_url[url]))
print('End of program')
'''
## removing special characters from a list of items in python

fname = ([re.sub('[^a-zA-Z]+', '', _) for _ in fname])
print(fname, fname_stamp)
f = open("c:/Users/admin/OneDrive/Documents/python-programs/images/" + ''.join(fname)+fname_stamp, "w")
db_name = "c:/Users/admin/OneDrive/Documents/python-programs/images/" +''.join(fname) + '.db'
names  = []
links  = []
p_txts = []

response = requests.get(url)
for page in range(1,157):
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


db = sqlite3.connect(db_name)
cursor = db.cursor()
cursor.executescript('drop table if exists imgs_links;')
cursor.execute('''
    #CREATE TABLE imgs_links(id INTEGER PRIMARY KEY, link TEXT, name TEXT, content TEXT)
''')
db.commit()

for i in range(0, len(links)):
    cursor.execute('''
#INSERT INTO imgs_links (id, link, name, content) VALUES (?,?,?,?)''',(i+1, links[i], names[i], p_txts[i]))
##print("End second part ... saving database")
##db.commit()
##db.close()
##f.close()
s.close()
s.quit()

