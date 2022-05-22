import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/kartik/Downloads/Drivers/geckodriver")

driver.get("http://www.facebook.com")

time.sleep(5)

email_box = driver.find_element_by_name("email")

#Returns True if the element is displayed, else return False
if (email_box.is_displayed() == True):
	print("Email box is displayed.")
else:
	print("Email box is not displayed.")

#Returns True if the element is enabled, else return False
if (email_box.is_enabled() == True):
	print("Email box is enabled.")
else:
	print("Email box is not enabled.")
	
password_box = driver.find_element_by_name("pass")

if (password_box.is_displayed() == True):
	print("Password box is displayed.")
else:
	print("Password box is not displayed.")
	
if (password_box.is_enabled() == True):
	print("Password box is enabled.")
else:
	print("Password box is not enabled.")

#send_keys used to send the text for the text fields
email_box.send_keys("FACEBOOK_EMAIL_ID")
password_box.send_keys("FACEBOOK_PASSWORD")

driver.find_element_by_name("login").click()

time.sleep(10)
driver.quit()
