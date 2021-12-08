# -*- coding: utf-8 -*-
# import libraries
# import urllib2
from bs4 import BeautifulSoup
import sys
import requests
import re
import csv

### Este es una prueba/tutorial
### el Web Site link:
### https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe


# las siguientes lineas eran para poder python2.7
# que el encoding no soportaba utf-8, ahora con python3.7 se usa
# "_*_ coding: utf-8 _*_" en el principio del codigo
#reload(sys)
#sys.setdefaultencoding('utf8')


# specify the url
#quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
quote_page = 'https://www.bloomberg.com/quote/CCMP:IND'
#quote_page = 'https://www.bloomberg.com/markets/stocks/world-indexes/americas' # Este link tiene tablas ...
print(quote_page,"\n")
# query the website and return the html to the variable 'page'
# page = urllib2.urlopen(quote_page)
# opener = urllib2.build_opener()
# opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
# response = opener.open(quote_page)
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# 
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US, en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6, la;q=0.5,pt;q=0.4,de;q=0.3', 'cache-control': 'max-age=0','upgrade-insecure-requests': '1', 
 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

#get web page text 
response = requests.get(quote_page, headers=headers).text
 

soup = BeautifulSoup(response, "html.parser")

# Referencia para re.compile que lo voy a usar mas adelante
# https://docs.python.org/2/library/re.html

# response = requests.get(quote_page, headers=headers)
# parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(response.text, 'html.parser')

# Take out the <div> of name and get its value
regex = re.compile(r'Name\B')
name_box = soup.findAll('div', attrs={'class': regex})
# soup return a list because used findAll
# verify len(name_box)
# name_box = soup.find('h1', attrs={'class': 'name'})

#name = name_box[0].text.strip() # strip() is used to remove starting and trailing
#print(name_box)

regex = re.compile(r'Price\B')
# get the index price
price_box = soup.findAll('div', attrs={'class':regex})

for i in range(len(name_box)):
    print(name_box[i].text,"\t\t\t",price_box[i].text)
    
#print(price_box)
'''
<meta itemprop="name" content="S&amp;P 500 Index">
<meta itemprop="tickerSymbol" content=" SPX">

<div class="schema-org-corporation" itemscope="" itemtype="http://schema.org/Corporation">
<meta itemprop="name" content="S&amp;P 500 Index">
<meta itemprop="url" content="https://www.bloomberg.com/quote/SPX:IND">
<meta itemprop="tickerSymbol" content=" SPX"></div>
<span class="companyId__87e50d5a">INDU:IND</span>
soup.find('table', { "class" : "wikitable sortable"})

>>> len(name_box)
5
>>> name = name_box[0].text.strip()
>>> name
'DJIA'
>>> name = name_box[1].text.strip()
>>> name
'S&P 500'
>>> name = name_box[2].text.strip()
>>> name
'NASDAQ'
>>> name = name_box[3].text.strip()
>>> name
'FTSE 100'
>>> name = name_box[4].text.strip()
>>> name
'NIKKEI 225 Future'
>>>
'''
