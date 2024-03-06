# Este codigo es para usar la respuesta de un search con imagenes
# y listas todos los urls de la imagenes y hacer download de ellas
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import datetime, time, re, requests, os, imghdr
# directorio donde guardar los file
chromedriver = 'C:\\Users\\jguis\\OneDrive\\chromedriver\\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

datafilepath = 'c:\\Users\\jguis\\OneDrive\\Documents\\python-programs\\images\\magazinecovers\\'
#datafilepath = 'c:\\Users\\admin\\OneDrive\\Documents\\python-programs\\images\\magazinecovers\\' ## when working in laptop
os.chdir(datafilepath)
fname_stamp = datetime.datetime.now().strftime("_%d%b%Y-%H%M")

#print(fname) ## DEBUG   

#nombre_de_archivo = ''.join(fname) # convert list to string
#print(fname+fname_stamp) #debugging
#driver = webdriver.Chrome() # this works in the laptop because the web driver is there
urly='https://duckduckgo.com/?q=fashion+magazine+covers&t=chromentp&iar=images&iax=images&ia=images'
urlx='https://duckduckgo.com/?q=time+magazine+covers&t=chromentp&iar=images&iax=images&ia=images'
url ='https://duckduckgo.com/?q=time%20magazine%20covers&t=chromentp&iax=images&ia=images'
url2='https://duckduckgo.com/?q=tech+magazine+covers&t=chromentp&iar=images&iax=images&ia=images'
url1='https://www.google.com/search?q=tech+magazine+covers&sca_esv=482705d0823fd1d6&sca_upv=1&source=hp&ei=q8HiZdylLfWvptQP08y0-Ao&iflsig=ANes7DEAAAAAZeLPu71v-8Q0U3kpDsDc6HL7W8qWpZUi&ved=0ahUKEwicp7u99NSEAxX1l4kEHVMmDa8Q4dUDCBs&oq=tech+magazine+covers&gs_lp=Egdnd3Mtd2l6IhR0ZWNoIG1hZ2F6aW5lIGNvdmVyc0gAUABYAHAAeACQAQCYAQCgAQCqAQC4AQzIAQCYAgCgAgCYAwCSBwA&sclient=gws-wiz'
url3='https://www.google.com/search?q=time+magazine+covers&tbm=isch&ved=2ahUKEwiP2O6Vp9WEAxV4mbAFHcIQDK0Q2-cCegQIABAA&oq=time+magazine+covers&gs_lp=EgNpbWciFHRpbWUgbWFnYXppbmUgY292ZXJzMgoQABiABBiKBRhDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIKEAAYgAQYigUYQzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI2m5Q0xlY5TVwAHgAkAEAmAGjAaAB5AqqAQMzLjm4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ8ICBhAAGAcYHsICBBAAGB7CAgYQABgIGB7CAggQABgIGAcYHogGAQ&sclient=img&ei=0vbiZY-nN_iywt0PwqGw6Ao&bih=569&biw=1280#imgrc=0XF2AkGmE9b0AM'
urlz='https://duckduckgo.com/?q=mens+magazine+covers&t=chromentp&iar=images&iax=images&ia=images'
urlw='https://duckduckgo.com/?q=newspaper+front+pages+today&t=chromentp&iar=images&iax=images&ia=images'

#driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get(urlw)
time.sleep(10)
driver.implicitly_wait(0.5)

html = driver.page_source
# use page title for db name and file name
fname = driver.title.title().split(' ') # changed every work to Title style
##print(fname," ",fname_stamp)
##print(f"{fname}{fname_stamp}") #debugging

# # removing special characters from a list of items in python
fname = ''.join([re.sub('[^a-zA-Z]+', '', _) for _ in fname])

soup = BS(html,'html.parser')
ffname = driver.title.title().split(' ')
ffname = ''.join(ffname[0:len(ffname)-2])

##print(title)
##print(fname)

imgUrls = re.findall('img .*?src="(.*?)"',html)
print(len(imgUrls))

#imgUrlsLinks = []

## save links to a file on current dir
## use os.path() to save in the home directory ~/python-programs
## to solve a issue of have different user names
with open(datafilepath+ffname+fname_stamp, 'a') as f:
  for lnks in imgUrls:
    f.write(lnks+'\n')

for fn in range(1,len(imgUrls)+1):
  try:
    response = requests.get("https:"+imgUrls[fn])
    extension = imghdr.what(file=None, h=response.content)
    save_file = ffname+f"-{fn}.{extension}"
    print(datafilepath+save_file,"","https://"+imgUrls[fn])
    with open(datafilepath+save_file,'wb') as f:
      f.write(response.content)
  except:
    print('error in url')
    

##for line in imgUrls:
##  imgUrlsLinks.append(line)
##
##for lnk in imgUrlsLinks:
##  print(lnk)

##selector = '#zci-images > div.js-tileview.tileview--grid > div.tile-wrap > div.zci__main.zci__main--tiles.js-tiles.has-nav.tileview__images.has-tiles--grid'


#text_box = driver.find_element(by=By.NAME, value="my-text")
##text_box = driver.find_element(by=By.CSS_SELECTOR, value="zci__main")
#submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#text_box.send_keys("Selenium")
#submit_button.click()

##message = driver.find_element(by=By.ID, value="#zci-images")
##text = message.text

driver.quit()
print('END')

'''
https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
https://stackoverflow.com/questions/13960326/how-can-i-parse-a-website-using-selenium-and-beautifulsoup-in-python
https://stackoverflow.com/questions/18408307/how-to-extract-and-download-all-images-from-a-website-using-beautifulsoup
https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
https://stackoverflow.com/questions/30229231/python-save-image-from-url

'''
