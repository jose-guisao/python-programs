## freeCodeCamp Tutorial
## https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/

import requests
from bs4 import BeautifulSoup



url = "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
##url = "https://www.libertaddigital.com/espana/politica/2022-08-09/la-indultada-maria-sevilla-crea-escuela-mi-expareja-ha-secuestrado-a-mi-hija-alena-de-2-anos-siguiendo-todos-sus-pasos-6922108/"
# Make the request

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# Create all_h1_tags as empty list

all_h1_tags = []

# Set all_h1_tags to all h1 of the soup

for element in soup.select('h1'):
  all_h1_tags.append(element.text)
  print(element)

# Create seventh_p_text ans set it to 7th p element text of the page

##seventh_p_text = soup.select('p').text
print("lenght" , soup.select('p'))

##print(all_h1_tags, seventh_p_text)
