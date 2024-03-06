#Selenium webdriver: How do I find ALL of an element's attributes?
#https://stackoverflow.com/questions/27307131/selenium-webdriver-how-do-i-find-all-of-an-elements-attributes
#You can find using element.get_property() method
#



from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.rottentomatoes.com/')
movie_button = driver.find_element(By.XPATH,'//*[@id="media-lists"]/div[1]/section/tiles-carousel-responsive-deprecated/tiles-carousel-responsive-item-deprecated[2]/tile-dynamic/button')
movie_image = driver.find_element(By.XPATH,'//*[@id="media-lists"]/div[1]/section/tiles-carousel-responsive-deprecated/tiles-carousel-responsive-item-deprecated[2]/tile-dynamic/rt-img')
attrs=[]
for attr in movie_button.get_property('attributes'):
    attrs.append([attr['name'], attr['value']])
print(attrs)
print("..clear list..")
attrs=[]
for attr in movie_image.get_property('attributes'):
    attrs.append([attr['name'], attr['value']])
print(attrs)
