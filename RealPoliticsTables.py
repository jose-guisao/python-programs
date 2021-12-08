#Este programa trata de sacar los polls de general elections de Realclearpolitics
#Este codigo tiene los primeros intentos de usar selenium
import urllib.request
##from bs4 import BeautifulSoup
from selenium import webdriver
##from selenium.webdriver.common.by import By
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import pandas as pd

#path = 'chromedriver'
#driver = webdriver.Chrome(path)
chromedriver = "H:/Downloads2/chromedriver/chromedriver.exe"
desired_capabilities=DesiredCapabilities.CHROME
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver,desired_capabilities=desired_capabilities)

url = 'https://www.realclearpolitics.com/epolls/latest_polls/general_election/'

driver.get(url)

title = driver.title # get page title
print("Page Title :",title)
##Find  //*[@id="my-nav"] to pass to next page
my_nav = driver.find_elements_by_xpath("//*[@id='my-nav']//*[contains(@id,'link')]")
num_of_pages = len(my_nav) # find how may links to move page
print("Numero de links/paginas: ",num_of_pages)
print("click page 1 .. and popup comes out...")
page_1 = my_nav[0].click()
time.sleep(5)
##page_2 = my_nav[1].click()
##time.sleep(10)
##page_3 = my_nav[2].click()

driver.implicitly_wait(15)
print("checking windows handlers")
alert = driver.switch_to.active_element
handle=driver.window_handles
##print(handle)
alert = driver.switch_to.window(handle[0])
print("select tab/page with tables..")
alert = driver.switch_to.active_element
print("switch to active page")
alert.click()
print("click the page")
my_nav = driver.find_elements_by_xpath("//*[@id='my-nav']//*[contains(@id,'link')]")
page_1 = my_nav[0].click()
container_tables = driver.find_elements_by_xpath("//*[@id='container']//*[contains(@id,'table')]")
container_tables_text0 = container_tables[0].text 
##print(container_tables_text0)

##my_nav_link_name = my_nav_link.get_attribute("href")
my_nav = driver.find_elements_by_xpath("//*[@id='my-nav']//*[contains(@id,'link')]")
##page_2 = my_nav[1].click()
print("waiting ...5 secs..")
time.sleep(5)
container_tables = driver.find_elements_by_xpath("//*[@id='container']//*[contains(@id,'table')]")
container_tables_text1 = container_tables[1].text 
##print(container_tables_text1)
##page_3 = my_nav[2].click()

#Este metodo trae un lista con el contenido de todas las tablas
#container_tables[i].text
container_tables = driver.find_elements_by_xpath("//*[@id='container']//*[contains(@id,'table')]")
container_tables_text2 = container_tables[2].text
##print(container_tables_text2)
##
##Test if last two characters are "\n"
##https://stackoverflow.com/questions/36686752/how-to-check-if-n-is-in-a-string
##if container_tables_text[-1:-2:-1] == '\n':
##    newerString = container_tables_text.strip()
##    print(newerString)
##else:
##    print(container_tables_text)
##    
total_tables = len(driver.find_elements_by_xpath("//*[@id='table-1']/table"))
print("Numero de tables :",total_tables)
#para verificar la cantidad de tablas
#Verificar cuantas lineas(rows) hay y cuantas columnas

row_count = len(driver.find_elements_by_xpath("//*[@id='table-1']/table[1]/tbody/tr"))
rows_total = len(driver.find_element_by_xpath("//*[@id='table-1']").find_elements_by_tag_name('tr'))
col_count = len(driver.find_elements_by_xpath("//*[@id='table-1']/table[2]/thead/tr/th"))
print("Number of rows :",rows_total ," Number of cols :",col_count)

header=""
table_header = driver.find_elements_by_xpath("//*[@id='table-1']/table[2]/thead/tr/th")
for hd in range(len(driver.find_elements_by_xpath("//*[@id='table-1']/table[2]/thead/tr/th"))):
    header_cell = table_header[hd].text
    header = header + '{:<47}'.format(header_cell)
print(" ",header)                                          
##print(table_header[0].text," ",table_header[1].text," ",table_header[2].text,table_header[3].text,'\n')
##print("start searching web elements..")
data_polls = []
for t in range(1, total_tables+1):
    tr_xpath = "//*[@id='table-1']/table[" + str(t) + "]/tbody/tr"
    if len(driver.find_elements_by_xpath("//*[@id='table-1']/table[" + str(t) + "]/tbody/tr/td")) == 1:
        print(driver.find_element_by_xpath("//*[@id='table-1']/table[" + str(t) + "]/tbody/tr/td").text)
        continue
    for r in range(1, len(driver.find_elements_by_xpath(tr_xpath))+1):
        row_data = ""
        td_xpath = tr_xpath + "[" + str(r) + "]/td"
        for d in range(1,len(driver.find_elements_by_xpath(td_xpath))+1):
            cell_data = driver.find_element_by_xpath(td_xpath + "[" + str(d) + "]").text
            row_data = row_data + '{:<47}'.format(cell_data)
        print('{:<2}'.format(t),row_data)
##    print("End of table : ",t) # ===> Debugging
print("End of program")

##driver.close()
##links = []
##elements = driver.find_elements_by_tag_name('a')
##for i in range(len(elements)):
##    link = elements[i].get_attribute("href")
##    links.append(link)
