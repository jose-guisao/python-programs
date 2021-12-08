try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "best python modules to install"

for j in search(query, tld="co.in", num=20, stop=20, pause=2):
	print(j)
