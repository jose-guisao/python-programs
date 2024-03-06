from bs4 import BeautifulSoup as BSoup
import requests, datetime, re, time
url = 'https://triponmag.com/23-the-most-beautiful-beaches-in-the-world/'
response = requests.get(url)

fname_stamp = datetime.datetime.now().strftime("_%d%b%Y-%H%M")
bs_obj = BSoup(response.content,'html.parser')
fname = bs_obj.title
# # removing special characters from a list of items in python
fname = ''.join([re.sub('[^a-zA-Z]+', '', _) for _ in fname])
print(fname, fname_stamp)
f = open("c:/Users/admin/OneDrive/Documents/python-programs/images/" + fname + fname_stamp, "a")
#db_name = "c:/Users/admin/OneDrive/Documents/python-programs/images/" +''.join(fname) + '.db'

f.write(bs_obj.prettify())

for i in range(1,24):
  response = requests.get(url + str(i) + '/')
  bs_obj = BSoup(response.content,'html.parser')
  f.write(bs_obj.prettify())
  time.sleep(2)
f.close()
print('End of programm..')
