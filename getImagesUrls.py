#/usr/bin/python3
# import urllib.request
import urllib.request
from bs4 import BeautifulSoup as BSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import re
chromedriver = "C:/Users/admin/Downloads/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
url1 = 'https://tenor.com/search/cat-gifs' # cats gifs
url = 'https://tenor.com/search/dog-gifs' # dogs gifs
bs_obj = BSoup(driver.page_source, 'html.parser')
response = urllib.request.urlopen(url)
req =  Request(url,headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
bs_obj = BSoup(webpage, 'html.parser')
driver.close()
images = bs_obj.findAll('img')
i=0
f = open("tenor-gif_urls-dogs.txt","w")

for image in images:
	i = i + 1
	# lnk = re.search('^http.*gif', image['src'] )
	# print(type(lnk.group(0)))
	f.write(image['src']+'\n')
	# print(i,image['src'])
print(len(images))

f.close()
f = open("tenor-gif_urls-dogs.txt",'r')
lines = f.readlines()
regex = r"^http.*.gif"

# https://regex101.com/r/evkgYU/1/
# las Lines que siguen despues del for loop son de este site, tiene un code generator

for line in lines:
	matches = re.finditer(regex,line)
	for matchNum, match in enumerate(matches, start=1):
		print("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
		for groupNum in range(0, len(match.groups())):
			groupNum = groupNum + 1
			print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
f.close()