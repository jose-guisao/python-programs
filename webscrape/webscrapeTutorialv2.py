import requests
from bs4 import BeautifulSoup
import re
url = "https://www.looper.com/1250805/every-one-blue-beetles-powers-abilities-explained/"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
print(soup.title.text)


galleryImagesHolder = soup.select('picture [src]')

## este selecciona un elemento en especifico
##galleryImages = soup.select("div.slide-key:nth-child(5) > picture:nth-child(1) > img:nth-child(3)")

##for lnk in soup.find_all('div', class_="gallery-image-holder"):
##  print(lnk)
idx=0
##for lnk in galleryImagesHolder:
##  print(lnk)
print(len(galleryImagesHolder))
print('....END....')
