import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

#Every function is same form radio buttons and checkboxes

serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

time.sleep(5)

#Accept the alert
alert = Alert(driver)
alert.accept()

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

#Dismiss the alert
alert = Alert(driver)
alert.dismiss()

time.sleep(3)

driver.quit()