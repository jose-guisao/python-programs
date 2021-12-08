# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
# specify the url
#urlpage = 'https://www.allmusic.com/album/praise-mw0000111206'
urlpage = 'https://www.allmusic.com/album/praise-worship-sampler-jubilee-mw0000111203'

print(urlpage)
# run firefox webdriver from executable path of your choice
driver = webdriver.Chrome(executable_path=r'C:/Users/jguisao/Downloads/chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(20)
#driver.quit()

# find elements by xpath

results = driver.find_elements_by_xpath("//*[@id='cmn_wrap']//*[@class='track']")


'''
results = driver.find_elements_by_xpath("

'''

print('Number of results', len(results))


# create empty array to store data
data = []
# loop over results
for result in results:
    team_name = result.text
    link = result.find_element_by_tag_name('a')
    team_link = link.get_attribute("href")
    # append dict to array
    data.append({"team" : team_name, "link" : team_link})

# close driver 

driver.quit()

# save to pandas dataframe
df = pd.DataFrame(data)
print(df)
