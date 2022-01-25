#/usr/bin/python3
import requests, re, time
from bs4 import BeautifulSoup as BSoup
from selenium import webdriver

chromedriver = 'C:/Users/admin/OneDrive/chromedriver/chromedriver.exe'
# driver = webdriver.Chrome(chromedriver)
url = 'https://stacker.com/stories/1173/celebrities-you-didnt-know-were-lgbtq'
url3 = 'https://kiwireport.com/celebrity-children-who-look-just-like-their-parents-did-at-the-same-age'
url4 = 'https://herbeauty.co/en/foodtravel/best-places-to-travel-in-2021'
url5 = 'https://investingfuel.com/entertainment/27-stars-from-the-90s-where-are-they-now'
url5_1 = 'https://investingfuel.com/entertainment/27-stars-from-the-90s-where-are-they-now/155'
url1 = 'https://tenor.com/search/cat-gifs'  # cats gifs
url2 = 'https://tenor.com/search/dog-gifs'  # dogs gifs
# driver.get(url5)
# time.sleep(3)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(4)
# bs_obj = BSoup(driver.page_source, 'html.parser')
response = requests.get(url5)
time.sleep(3)
bs_obj = BSoup(response.text, 'html.parser')
images1 = bs_obj.findAll('img')
print(len(images1))
# driver.get(url5_1)
# time.sleep(3)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(4)
# bs_obj = BSoup(driver.page_source, 'html.parser')
response = requests.get(url5_1)
time.sleep(3)
bs_obj = BSoup(response.text, 'html.parser')

images2 = bs_obj.findAll('img')
print(len(images2))
#Usar el title de la pagina para crear el filename, pero eliminando todo especial characters
fname = bs_obj.title
print(fname)

# # removing special characters from a list of items in python
# fname = ([re.sub('[^a-zA-Z0-9]+', '', _) for _ in fname])
# print(fname)
# f = open(''.join(fname), "w")
i = 0
for image in images1 + images2:
    i = i + 1
    # lnk = re.search('^http.*gif', image['src'] )
    # print(type(lnk.group(0)))
    # f.write(image['src'] + '\n')
    print(i, image['src'])
print(len(images2))
