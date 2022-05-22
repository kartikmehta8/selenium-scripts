import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("https://www.kartikmehta.engineer/")

driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/div[2]/a[3]").click()

#Returns a unique id for the tab
print(driver.current_window_handle)

#Returns the id for each and every tab opened in the browser
ids = driver.window_handles
for i in ids:
	#Switch to the particular window
	driver.switch_to.window(i)
	print(driver.title)
	print(driver.current_window_handle)
	if driver.title == "Kartik Mehta":
		driver.close()

time.sleep(3)

driver.quit()