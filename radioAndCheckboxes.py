import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Every function is same form radio buttons and checkboxes

serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("https://demoqa.com/automation-practice-form")

#Returns true if radio button is selected, false otherwise
status_male_radio = driver.find_element(By.ID, "gender-radio-1").is_selected()

if (status_male_radio == True):
	print("Male radio button is selected")
else:
	print("Male radio button is not selected")

try:
	element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gender-radio-1"))
    )
	driver.find_element(By.ID, "gender-radio-1").click()

except:
	print("Something went wrong")
	driver.quit()

status_male_radio = driver.find_element(By.ID, "gender-radio-1").is_selected()

if (status_male_radio == True):
	print("Male radio button is selected")
else:
	print("Male radio button is not selected")

driver.quit()
