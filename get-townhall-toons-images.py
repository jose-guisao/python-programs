import requests, datetime, sqlite3, re, time


def download_file(url):
    local_fname = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("c:/Users/admin/OneDrive/Documents/python-programs/images/"+local_fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_fname

f = open("c:/Users/admin/OneDrive/Documents/python-programs/images/PoliticalCartoons_28Jan2022-2343", "r")

for link in f.readlines():
    url = 'http:' + link.rstrip()
    download_file(url)
    print('http:' + link)
