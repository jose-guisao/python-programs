#wp-block-image

#'https://stoppingsocialism.com/2021/11/top-100-conservative-websites-november-2021/'
from bs4 import BeautifulSoup, SoupStrainer
import requests

url = "https://stoppingsocialism.com/2021/11/top-100-conservative-websites-november-2021/"
page = requests.get(url)
data = page.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))

