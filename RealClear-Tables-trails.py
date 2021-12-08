#Este programa trata de sacar los polls de general elections
#de Realclearpolitics
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import pandas as pd
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
print("Click page 1 ...")## for debugging
page_0 = my_nav[0].click()
print("Waiting 5 secs...")## for debugging
time.sleep(5)
##page_1 = my_nav[1].click()
##time.sleep(10)
##page_2 = my_nav[2].click()
print("waiting ... 10 secs")## for debugging
driver.implicitly_wait(10)

alert = driver.switch_to.active_element
handle=driver.window_handles
#print(handle)
print("Switch window ..")## for debugging
alert = driver.switch_to.window(handle[0])
alert = driver.switch_to.active_element
alert.click()

my_nav = driver.find_elements_by_xpath("//*[@id='my-nav']//*[contains(@id,'link')]")
print("Click active window .. ") ## for debugging
page_0 = my_nav[0].click()
total_tables1 = len(driver.find_elements_by_xpath("//*[@id='table-1']/table"))
container_tables = driver.find_elements_by_xpath("//*[@id='container']//*[contains(@id,'table')]")
container_tables_text0 = container_tables[0].text 
table_data = []
table_data.append(title) ## Add title to list
table_data.append('\n')
##for table in range(1,len(driver.find_elements_by_xpath("//*[@id='table-1']/table"))+1):
##    table_xpath = "//*[@id='table-1']/table["+str(table)+"]"
##    row_xpath = table_xpath + "/tbody/tr"
##    col_xpath = row_xpath + "/td" ### retorna el total de celdas por tabla
##    print("table no.: ",table,len(driver.find_elements_by_xpath(row_xpath)),"",len(driver.find_elements_by_xpath(col_xpath)))

for table in range(1,len(driver.find_elements_by_xpath("//*[@id='table-1']/table"))+1):
    rows_xpath = "//*[@id='table-1']/table[" + str(table) + "]/tbody/tr" ## ==> "//*[@id='table-1']/table[1]/tbody/tr"
    rows_len = len(driver.find_elements_by_xpath(rows_xpath))
    for tr in range(1,len(driver.find_elements_by_xpath("//*[@id='table-1']/table[" + str(table) + "]/tbody/tr"))+1):
        cols_xpath = rows_xpath + "[" + str(tr) + "]/td"
##        if rows_len == 1:
##            poll_date = driver.find_element_by_xpath("//*[@id='table-1']/table" + "[" + str(table) + "]/tbody" + "/tr").text
##            print(poll_date)
##            continue
        poll_date = driver.find_element_by_xpath("//*[@id='table-1']/table" + "[" + str(table) + "]/tbody" + "/tr").text
        print(table," ",poll_date)
        for td in range(1,len(driver.find_elements_by_xpath("//*[@id='table-1']/table" + "[" + str(table) + "]/tbody" + "/tr[" + str(tr) + "]"))):
            print("For loop td")
            for cell_data in range(1,len(driver.find_elements_by_xpath("//*[@id='table-1']/table" + "[" + str(table) + "]tbody" + "/tr[" + str(tr) + "]" + "/[" + str(td) + "]"))):
                cell_dat = driver.find_element_by_xpath("//*[@id='table-1']/table" + "[" + str(table) + "]tbody" + "/tr[" + str(tr) + "]" + "/[" + str(td) + "]").text
                row_data = row_data + '{:15}'.format(cell_dat)
            print('{:>2}'.format(table)," ",row_data)
    
##for table in range(1,len(driver.find_elements_by_xpath("//*[@id='table-1']/table"))+1):
##    table_xpath = "//*[@id='table-1']/table["+str(table)+"]"
##    row_xpath = table_xpath + "/tbody/tr"
##    col_xpath = row_xpath + "[1]/td" ###  retorna la cantidad de columnas por tabla
####    print("table no.: ",table,len(driver.find_elements_by_xpath(row_xpath)),"",len(driver.find_elements_by_xpath(col_xpath)))
####//*[@id="table-1"]/table[4]/tbody/tr[1]/td[1]
##    for tr in range(1,len(driver.find_elements_by_xpath(row_xpath)) + 1):
##        xpath1 = row_xpath + "[" + str(tr) + "]"
##        for td in range(1,len(driver.find_elements_by_xpath(col_xpath)) + 1):
##            xpath2 = xpath1 + "/td[" + str(td) + "]"
####            print(driver.find_element_by_xpath(xpath2).text)
##            table_data.append(driver.find_element_by_xpath(xpath2).text)
##            if len(driver.find_elements_by_xpath(col_xpath)) == td:
##                table_data.append("\r\n")
####    if table == 5: ## for debugging
####        break
##print("Saving data to tableDataFile.txt file ...")
##                
##with open('tableDataFile.txt','w') as f:
##    f.write('\n'.join(table_data))
##f.close()
print("Clossing Browser ..")
driver.close()
driver.quit()

print("END")
## Añadir Pandas
