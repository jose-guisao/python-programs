from datetime import datetime
from bs4 import BeautifulSoup as BSoup
import requests
import time
url = 'https://townhall.com/political-cartoons'
url1 = 'https://townhall.com/political-cartoons/2022/01/27'
day = input('Enter day number:')
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
