# See information on https://www.geeksforgeeks.org/python-beautifulsoup-find-all-class/

from bs4 import BeautifulSoup
# import urllib2
import urllib
import requests
# homepage = urllib2.urlopen('https://www.rottentomatoes.com')
# homepage = urllib.request.urlopen('https://www.rottentomatoes.com')

homepage = urllib.request.urlopen(
    'https://www.rottentomatoes.com/browse/in-theaters/')
soup = BeautifulSoup(homepage.read(), 'html.parser')
top_box_office_list = soup.find(class_="body")
# print(top_box_office_list)

# The task is to write a program to find all the classes for a given Website URL.
#  In Beautiful Soup there is no in-built method to find all classes.

# method two
# website URL for rottentomatoes box-office
URL = 'https://www.rottentomatoes.com/browse/in-theaters/'
# class list set
class_list = set()
# page content from website URL
page = requests.get(URL)
# parse html content
soup = BeautifulSoup(page.content, 'html.parser')
# get all tags
tags = {tag.name for tag in soup.find_all()}
# iterate all tags
for tag in tags:

    # find all elements of tag
    for i in soup.find_all(tag):

        # if tag has attribute of class
        if i.has_attr("class"):

            if len(i['class']) != 0:
                class_list.add(" ".join(i['class']))
print(class_list)
# print(type(soup))
# first we use the find method to retrieve the table with 'Top-Box-Office' id
# top_box_office_table = soup.find('table', {'id': 'Top-Box-Office'}) # The original webpage apparently had Top-Box-office in the main page
# top_box_office_table = soup.find(
#     'div', {'id': 'content-column'})


# print(top_box_office_table)
# then we iterate over each row and extract movies information
# for row in top_box_office_table.find_all('tr'):
# cells = row.find_all('td')
# title = cells[1].find('a').get_text()
# money = cells[2].find('a').get_text()
# score = row.find('span', {'class': 'tMeterScore'}).get_text()
# print('{0} -- {1} (TomatoMeter: {2})'.format(title, money, score))
#
