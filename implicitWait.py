import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/kartik/Downloads/Drivers/geckodriver")

driver.get("https://www.facebook.com/")

#Browser will wait for specified seconds if the statement execution is taking time
driver.implicitly_wait(10)
#1. It is applicable to all the elements
#2. It can be only specified one time at the beginning of the code

#The assert statement is used to continue the execute if the given condition evaluates to True. If the assert condition evaluates to False, then it raises the AssertionError exception with the specified error message.
assert "Facebook – log in or sign up" in driver.title


email_box = driver.find_element(By.NAME, "email")
password_box = driver.find_element(By.NAME, "pass")

email_box.send_keys("FACEBOOK_EMAIL_ID")
password_box.send_keys("FACEBOOK_PASSWORD")

driver.find_element(By.NAME, "login").click()

time.sleep(10)

driver.quit()
