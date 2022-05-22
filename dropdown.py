import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Every function is same form radio buttons and checkboxes

serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("https://demoqa.com/automation-practice-form")

dropdown = Select(driver.find_element(By.ID, "ID_TO_SELECT"))

#Select by visible text
dropdown.select_by_visible_text("Morning")

#Select by index
dropdown.select_by_index(2)

#Select by value
dropdown.select_by_value("VALUE_TO_OPTION")

#Count number of options
print(len(dropdown.options))

#Capture all options and print as output
all_options = dropdown.options
for option in all_options:
	print(option.text)
