# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
# specify the url
urlpage = 'https://www.nba.com/standings' 
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
#results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='team active']//*[@class='title teamTitle']")
#results = driver.find_elements_by_xpath("//*[@id='block-league-content']//*[contains(@id,'nba-table')]")
results = driver.find_elements_by_xpath("//*[@id='block-league-content']//*[@class='cell-team pinned']")

##results = driver.find_elements_by_xpath("//*[@id='block-league-content']//*[@class='cell-team pinned']")
#"//input[@name='username']")

#results = driver.find_elements_by_xpath("//*[@id='block-league-content']//*[@class='hide-for-small-only']")
#<table class="conference east"> <thead> <a href="show-for-sr"> <td class="cell-win unpinned">

#results = driver.find_elements_by_xpath("//th[@class='cell-team pinned']")

#//*[@id="block-league-content"]/standings/section[2]/nba-table[1]/div/div
#//*[@id="block-league-content"]/standings/section[2]
#//*[@id="block-league-content"]/standings/section[2]/nba-table[1]/div/div/table/tbody/tr[1]/th

'''
results = driver.find_elements_by_xpath("
//*[@id='componentsContainer']
//*[contains(@id,'listingsContainer')]
//*[@class='product active']
//*[@class='title productTitle']")
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

#driver.quit()

# save to pandas dataframe
df = pd.DataFrame(data)
print(df)
