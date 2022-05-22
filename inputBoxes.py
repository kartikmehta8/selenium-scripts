import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("https://demoqa.com/automation-practice-form")

#To find how many input boxes present in the webpage?
inputBoxesCount = driver.find_elements(By.CLASS_NAME, "form-control")

print(len(inputBoxesCount))

#How to provide value to the textbox?

driver.find_element(By.ID, "firstName").send_keys("Kartik")
driver.find_element(By.ID, "lastName").send_keys("Mehta")
driver.find_element(By.ID, "userNumber").send_keys("987654321")

time.sleep(5)

#is_displayed returns true when the object is displayed, false otherwise
#is_enabled return true when the object is enabled, false otherwise

driver.quit()
