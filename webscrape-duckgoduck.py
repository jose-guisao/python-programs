import requests
query = "tech+magazine+front+page+photo&t=newext&atb=v284-1&iar=images&iax=images&ia=images"
page = requests.get("https://duckduckgo.com/?q=" + query)
print(page.text)
