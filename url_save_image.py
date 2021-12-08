from urllib import request
import urllib
import sqlite3
url = ""

db = sqlite3.connect('ImagesLinksDataBase.db')
cursor = db.cursor()
sql = 'SELECT link from img_links;'
url_data = cursor.execute(sql)
data = url_data.fetchone()

image = urllib.request.urlretrieve(''.join(data),'file003.jpg')
