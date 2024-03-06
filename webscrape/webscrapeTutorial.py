import requests
from bs4 import BeautifulSoup
import soupsieve as sv
# make the request
urls = [
    "https://www.looper.com/205738/underrated-netflix-gems-to-add-to-your-must-watch-list/",
    "https://www.looper.com/471652/best-movies-all-time/"
]

urls1 = [
    "https://www.looper.com/1250805/every-one-blue-beetles-powers-abilities-explained/"
]
# ,
#     "https://www.looper.com/227221/the-real-reason-we-havent-seen-these-dc-characters-in-the-dceu-yet/"
# ]


def getwebpage(urls):

    for url in urls:
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html5lib')
        # print(soup.select('h1.title-gallery')[0].text)
        # using soupsieve
        print(sv.select('img:is(.gallery-image)', soup))
        # for lnk in soup.select('h2'):
        # print(lnk.text)
        for lnk in sv.select('img:is(.gallery-image)', soup):
            print(lnk)


# def getimglink(webpage):
#     # toma la data que tiene la variable soup como arg
#     for lnk in soup.select('picture'):
#         print(lnk.text)

getwebpage(urls1)
