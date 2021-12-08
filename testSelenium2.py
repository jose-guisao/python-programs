# Import your newly installed selenium package
from selenium import webdriver

# Now create an 'instance' of your driver
# This path should be to wherever you downloaded the driver
driver = webdriver.Chrome(executable_path=r'C:/Users/jguis/Downloads/chromedriver/chromedriver.exe')
# A new Chrome (or other browser) window should open up

# Now just tell it wherever you want it to go
driver.get("https://medium.com/@dalewahl")
# Return the title
# Good to use assert clause to make sure you are where you think you are
driver.title

# Navigate back and forward with the browser buttons just like a real human!
driver.back()
driver.forward()

# Save a screenshot; check and see what was going on or capture something specific
driver.save_screenshot('test_shot.png')

# Ah, pull all the code onto your machine
driver.page_source
# This is where you get that sweet, sweet data
# Sort it with some BeautifulSoup tools and store it away!

# You'll also likely want to move around and click some links
driver.find_element_by_link_text('text you want to find')
driver.find_element_by_partial_link_text('part of the text')
# add an 's' to element if you want to return a whole list of elements

# Add this method to click it!
driver.find_element_by_link_text('text you want to find').click()

# You also may want to type into fields
driver.find_element_by_name(textbox).send_keys('type this in, robot')

# Here are some other things you may want to find (look for them in the HTML code):
'''
.find_element_by_id()
.find_element_by_name()
.find_element_by_xpath()
.find_element_by_tag_name()
.find_element_by_class_name()
.find_element_by_css_selector()
'''
#Finally, don't forgot to close your webdriver when done
driver.close()
