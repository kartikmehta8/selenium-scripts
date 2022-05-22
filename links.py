import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("https://www.facebook.com/")

links = driver.find_elements(By.TAG_NAME, "a")

#To count the number of links
print(len(links))

#To print all the links
for link in links:
	print(link.text)

#Clicking on the link
driver.find_element(By.LINK_TEXT, "Forgotten password?").click()

time.sleep(5)

driver.quit()
