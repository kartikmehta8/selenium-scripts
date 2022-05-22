import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("https://leetcode.com/")

time.sleep(5)
print("Leetcode opened Successfully")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]").click()

time.sleep(10)
print("Navigated to Sign-up page")

driver.find_element(By.XPATH, "//*[@id='id_login']").send_keys("LEETCODE_USERNAME")
driver.find_element(By.XPATH, "//*[@id='id_password']").send_keys("LEETCODE_PASSWORD")
print("Entered the credentials")

time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='signin_btn']").click()

time.sleep(15)
print("Signed in to your account")

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/a").click()

time.sleep(5)
print("Navigated to all problemsets")

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/a").click()

time.sleep(10)
print("Successfully opened the question")

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/div[2]/div/button").click()

time.sleep(5)
print("Submitted the unsuccessful code")

time.sleep(5)
print("Closing the browser")

driver.quit()
