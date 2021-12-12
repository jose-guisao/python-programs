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

url = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=Inflight+Items" 

print(get_item_page(url))
response = requests.get(url)
doc = BeautifulSoup(response.text,'html.parser')

print(doc)

