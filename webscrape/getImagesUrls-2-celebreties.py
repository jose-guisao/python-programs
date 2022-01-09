#/usr/bin/python3
import requests
from bs4 import BeautifulSoup as BSoup
from selenium import webdriver
import re

chromedriver = 'C:/Users/admin/OneDrive/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
url = 'https://stacker.com/stories/1173/celebrities-you-didnt-know-were-lgbtq'
url1 = 'https://tenor.com/search/cat-gifs' # cats gifs
url2  = 'https://tenor.com/search/dog-gifs' # dogs gifs
bs_obj = BSoup(driver.page_source, 'html.parser')
response = requests.get(url)
bs_obj = BSoup(response.text, 'html.parser')
driver.close()
images = bs_obj.findAll('img')
i=0
#Usar el title de la pagina para crear el filename, pero eliminando todo especial characters
fname = bs_obj.title
# removing special characters from a list of items in python
fname = ([re.sub('[^a-zA-Z0-9]+', '', _ ) for _ in fname])
print(fname)
f = open(''.join(fname),"w")

for image in images:
	i = i + 1
	# lnk = re.search('^http.*gif', image['src'] )
	# print(type(lnk.group(0)))
	f.write(image['src']+'\n')
	# print(i,image['src'])
print(len(images))

f.close()

f = open(''.join(fname),'r')
lines = f.readlines()
# regex = r"^http.*.gif"
regex = r"^http.*.png"
# https://regex101.com/r/evkgYU/1/
# https://regex101.com/r/evkgYU/1/codegen?language=python

# las Lines que siguen despues del for loop son de este site, tiene un code generator

for line in lines:
	matches = re.finditer(regex,line)
	for matchNum, match in enumerate(matches, start=1):
		print("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
		for groupNum in range(0, len(match.groups())):
			groupNum = groupNum + 1
			print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
f.close()
