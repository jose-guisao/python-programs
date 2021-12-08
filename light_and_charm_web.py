import urllib.request
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import pandas as pd

chromedriver = "C:/Users/jguis/Downloads/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(chromedriver)

url = 'http://lightandcharm.com/the-most-remarkable-oscars-outfits-ever/?utm_source=taboola&utm_term=disqus-widget-cnsnews_1055390&utm_content=211658555_http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2Fc40d432ccab4a55cb6b2cc8326f45a0a.png_The+Most+Unforgettable+Oscars+Outfits+Of+All+Time_Desktop_2019-06-09+02%3A43%3A43&utm_medium=referral&utm_campaign=OscarsOutfits-All-DTM-LNC-TB'
url2 = 'http://readysethealth.com/unreal-photos-korea/3/'
driver.get(url2)
title = driver.title # get page title

print("Page Title :",title)
