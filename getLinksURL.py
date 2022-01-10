#wp-block-image

#'https://stoppingsocialism.com/2021/11/top-100-conservative-websites-november-2021/'
from bs4 import BeautifulSoup, SoupStrainer
import requests
from datetime import datetime
filename1 = ("drudgereport-" + datetime.now().strftime("%Y%m%d-%H%M%S"))
fname = open(filename1 + '.url', 'w')
url   = "https://stoppingsocialism.com/2021/11/top-100-conservative-websites-november-2021"
url1 = 'https://drudgereport.com'
page = requests.get(url1)
data = page.text

soup = BeautifulSoup(data,'html5lib' )

for link in soup.find_all('a'):
    fname.write(link.get('href')+'\n')
fname.close()
