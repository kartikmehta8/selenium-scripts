import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/kartik/Downloads/Drivers/geckodriver")

driver.get("http://demo.automationtesting.in/Windows.html")

#Printing title
print(driver.title)

#Printing URL
print(driver.current_url)

#Clicking a button by finding element by XPath
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

time.sleep(5)

#Closes one tab at a time - If two tabs are opened, then it will close the parent window
#If one tab is opened in a browser, it will close the bowser
driver.close()

#Quits the browser by closing all the tabs
driver.quit()
