from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.nba.com/standings'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
table = soup.findAll('div', {'class': 'details'})

f = open('nba-standing.txt', 'w')
f.write(str(soup))

# La tabla de NBA-Standing no sale en el html !!!
# If you need to get content generated dynamically by JavaScript
# and you don't want to use Selenium, you can try requests-html
# tool that supports JavaScript:

session = HTMLSession()
r = session.get(url)
r.html.render()  # no se que hace render() !!


# para copiar una pagina web en un file
r = session.get(url)

with open('example.html', 'wb') as f:
    f.write(r.content)
f.close()
