#Include in every file
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/kartik/Downloads/Drivers/geckodriver")

driver.get("https://www.kartikmehta.engineer")

#printing title of he page
print(driver.title)

#Capturing the current URL
print(driver.current_url)

#HTML Code for the page
print(driver.page_source)

#Quitting the browser
driver.close()
