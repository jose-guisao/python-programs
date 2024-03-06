
import requests
import urllib
from bs4 import BeautifulSoup

url = 'https://aranchmom.com/10-new-years-resolutions-christians/#:~:text=10%20New%20Years%20Resolutions%20for%20Christians%20in%202024,8%208.%20Pray%20every%20day%20...%20M%C3%A1s%20elementos'

session = requests.session()
session.headers.update({
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
  'Accept': '*/*',
  'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
  'Content-Type': 'application/json',
  'Origin': 'https://auth.fool.com',
  'Connection': 'keep-alive',
  })

response = session.get(url)

data =  BeautifulSoup(response.text,'html.parser')
my_h3 = data.find_all("h3")
for h3 in my_h3:
  print(h3.text)
