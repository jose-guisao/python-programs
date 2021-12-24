# https://blog.jovian.ai/web-scraping-with-requests-beautifulsoup-and-selenium-30b8f77a6f62
import requests
from random import randint
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd


def get_item_page(items_url):
    # Download the page
    response = requests.get(items_url)
    # check succesul response
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(items_url))
        # Parse using Beautiful soup
        doc = BeautifulSoup(response.text,'html.parser')
        return doc

#Now we have a summarised above steps in a function as below
def get_item_list_tags():
    item_list_tags = []
    for page in range(1,5):
          items_url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=Inflight+Items&viewtype=G&tab={page}"
          response = requests.get(items_url)
          page_contents = response.text
          if response.status_code != 200:
              raise Exception('Failed to load page {}'.format(items_url))
          doc = BeautifulSoup(page_contents, "html.parser")
          for item in doc.find_all("div", {'class': "organic-gallery-offer-outter J-offer-wrapper"}):
                item_list_tags.append(item)
          sleep(randint(1,10))
          print('Downloading page number', page)  
    return item_list_tags
item_list_tag = get_item_list_tags()
print(len (item_list_tag))

url = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=Inflight+Items" 


# page = get_item_page(url)
# response = requests.get(url)
# doc = BeautifulSoup(response.text,'html.parser')
# print(response.status_code)
# print(doc.prettify())
# print(page)
