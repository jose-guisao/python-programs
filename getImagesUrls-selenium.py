# import urllib.request
from bs4 import BeautifulSoup as BSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import re
chromedriver = "H:/Downloads2/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
url0 = 'http://readysethealth.com/20-celebrities-you-didnt-know-were-lgbtq/2/'
url1 = 'https://pjmedia.com/trending/top-conservative-websites-for-2018/'
url2 = 'https://www.drudgereport.com/'
url3 = 'http://readysethealth.com/these-celebrity-kids-look-just-like-their-parents-at-the-same-age/'
url4 = "https://www.buzzfeed.com/xfinity/literally-just-gifs-of-cats-tbh"
driver.get(url4)
req =  Request(url4,headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
bs_sel_obj = BSoup(driver.page_source, 'html.parser')
bs_obj = BSoup(webpage, 'html.parser')
print(bs_obj.find('title').text)
# images = bs_obj.findAll('img')
# images = bs_obj.findAll('a',href=True)
for a in bs_obj.findAll('a',href=True):
    print("Found the URL:",a['href'])
    
i=0
# for image in images:
	# i = i + 1
	# print(i,image['src'])
# print(len(images))
# driver.close()
# driver.quit()

'''
//*[@id="post-15013"]/div/div[3]/a
for i in  elements:
    image = i.find_element_by_tag_name("img")
    img_src = image.get_attribute("src")
    '''
