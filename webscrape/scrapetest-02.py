from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# This is an example from book WebScraping with python


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
        # return a null, break, or do some other plan "B"
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

# ejemplo de como extraer tags ...
# En este ejemplo la pagina usa color rojo (<span class="red">) para el dialogo de los personajes
# y usa el color verde (<span class="green">) para los nombres de personajes


def getNameList(bsObj):
    nameList = bsObj.find_all("span", {"class": "green"})
    return nameList


def getPageContent(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    return bsObj


url = "http://www.pythonscraping.com/pages/warandpeace.html"
title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)

pageInfo = getPageContent(url)
namelist = getNameList(pageInfo)
for name in namelist:
    # .get_text() strips all tags from document and return string with text only
    print(name.get_text())

print("\n..Fin..\n")
