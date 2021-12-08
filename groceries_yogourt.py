# import libraries
import urllib.request
from bs4 import BeautifulSoup

# specify the url
urlpage = 'https://groceries.asda.com/search/yogurt' 

print(urlpage)

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# find product items
results = soup.find_all('div', attrs={'class': 'listing category_templates clearfix productListing'})

print('Number of results', len(results))
