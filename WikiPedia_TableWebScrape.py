#https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722
#Tutorial :
#Web Scraping Wikipedia Tables using BeautifulSoup and Python

from bs4 import BeautifulSoup
import requests
import pandas as pd

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text
soup = BeautifulSoup(website_url,'html')
#print(soup.prettify())
Mytable = soup.find('table',{'class':'wikitable sortable'})
links =  Mytable.findAll('a')
#print(links)

Countries = []
for link in links:
    Countries.append(link.get('title'))
#print(Countries)    

df = pd.DataFrame()
df['Country'] = Countries

print('saving file ... ')
with open('wikiwebScrapeSite.html','w',encoding="utf-8") as f:
    f.write(str(soup.prettify()))
f.close()
with open('wikiwebScrapeSite_lst.txt','w') as f:
    f.write(str(Countries))
f.close()
with open('wikiwebScrapeSite_pd.txt','w') as f:
    f.write(str(df))
f.close()
