import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/kartik/Downloads/Drivers/geckodriver")

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

driver.get("https://www.kartikmehta.engineer")
print(driver.title)

time.sleep(5)

#Go to previous opened page
driver.back()
print(driver.title)

#Go to next opened page
driver.forward()
print(driver.title)

time.sleep(5)

driver.quit()
