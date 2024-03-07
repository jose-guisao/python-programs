from selenium import webdriver
##from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import datetime, time, re, requests, os, imghdr
chromedriver = 'C:\\Users\\jguis\\OneDrive\\chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
# driver = webdriver.Chrome()

# create a timestamp to added to filename
fname_stamp = datetime.datetime.now().strftime("_%d%b%Y-%H%M")

# This path is used from python runing in laptop
# I should find a way to use a %homedir% to overcome the issue of running from a different PC
# In this case the user admin is not the same on the desktop PC
# datafilepath = "c://Users//admin//OneDrive//Documents//python-programs//images//magazinecovers//"
datafilepath = "c://Users//jguis//OneDrive//Documents//python-programs//images//positiveQuotes//"
os.chdir(datafilepath)
## Urls copied from search engine duckduckgo
query = input("Enter search entries separeted by space: ")
url2='https://duckduckgo.com/?q=tech+magazine+covers&t=chromentp&iar=images&iax=images&ia=images'
url1='https://duckduckgo.com/?t=h_&q=Positive+Quotes&iax=images&ia=images'
url3='https://duckduckgo.com/?q=mensajes+positivos+cristianos&t=h_&iax=images&ia=images'
url4='https://duckduckgo.com/?q=mensajes+cristianos+cortos&t=newext&atb=v284-1&iar=images&iax=images&ia=images'
driver.get(url4)
time.sleep(10)
driver.implicitly_wait(0.5)
html = driver.page_source
titulo = driver.title.title().split(' ')
#Usar el titulo de la pagina para el nombre del filename

fname = ''.join(titulo[0:len(titulo)-2]) #file name with timestamp
fname = ''.join([re.sub('[^a-zA-Z]+', '', _) for _ in fname])+fname_stamp
##imgUrls = re.findall('img .*?src="(.*?)"',html) # to find all images links using regex , dont bring the http://

## Los siguientes queries son de prueba. Tengo que verificar como extraer
## la informacion del Grid, cada elemento ie. img y el texto
##html_element1 = driver.find_elements(By.TAG_NAME, "a")
##
##html_element0 = driver.find_elements(By.CLASS_NAME, "tile")
##
##html_element2 = driver.find_element(By.CLASS_NAME, "tile-wrap  .zci__main")
##
##html_element3 = driver.find_elements(By.CLASS_NAME, "tile-wrap  .zci__main .tile")
##
##html_element4 = driver.find_elements(By.CLASS_NAME, "tile-wrap  .zci__main .tile .tile--img__media")

# este css-selector es copiado del browser dev-tools copy css selector pero le elimine parte
##zci-images > div > div.tile-wrap >
##div.zci__main.zci__main--tiles.js-tiles.has-nav.tileview__images.has-tiles--grid >
##div:nth-child(3) >
##div.tile--img__media > span > img
html_elem5 = driver.find_elements(By.CSS_SELECTOR, "div.tile--img__media > span > img") 
#zci-images > div > div.tile-wrap > 
with open(datafilepath+fname+'.txt','a') as f:
  for i in range(0,len(html_elem5)):
    f.write(html_elem5[i].get_attribute('src')+'\n')


for fn in range(1,len(html_elem5)+1):
  try:
    response = requests.get(html_elem5[fn].get_attribute('src'))
    extension = imghdr.what(file=None, h=response.content)
    save_file = fname+f"-{fn}.{extension}"
    print(datafilepath+save_file,"","https://"+html_elem5[fn].get_attribute('src'))
    with open(datafilepath+save_file,'wb') as f:
      f.write(response.content)
  except:
    print('error in url')

print(titulo)
print('dimension de la lista de urls ',len(html_elem5))
print("..END..")
driver.close()
