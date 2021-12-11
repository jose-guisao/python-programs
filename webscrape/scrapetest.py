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


url = "http://www.pythonscraping.com/exercises/exercise.html"
title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)
