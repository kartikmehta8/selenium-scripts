import time

from curses.ascii import isalpha
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_name_from_email(email):
    s_intermediate = ""
    for i in email:
        if(i != '@'):
            s_intermediate += i
        else:
            break
    s = ""
    for i in s_intermediate:
        if (isalpha(i) == True):
            s += i
    return s

email = input("Enter the email : ")
name = get_name_from_email(email)

serv = Service("/home/kartik/Downloads/Drivers/geckodriver")

driver = webdriver.Firefox(service = serv)

driver.get("https://www.linkedin.com/")
time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='session_key']").send_keys("LINKEDIN_EMAIL_ID")
driver.find_element(By.XPATH, "//*[@id='session_password']").send_keys("LINKEDIN_PASSWORD")
driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/button").click()
time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div[6]/header/div/div/div/div[1]/input").send_keys(name)
driver.find_element(By.XPATH, "/html/body/div[6]/header/div/div/div/div[1]/input").send_keys(Keys.ENTER);
time.sleep(10)

people = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/section/div/nav/div/ul/li[2]/button")
if (people.text == "People"):
    people.click()
else:
    people = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/section/div/nav/div/ul/li[1]/button")
    people.click()

time.sleep(10)

link_test = driver.find_element(By.CSS_SELECTOR, "li.reusable-search__result-container:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a").get_attribute("href")
print(link_test)

all_links = driver.find_elements(By.CLASS_NAME, "app-aware-link")
for link in all_links:
    a_link = link.get_attribute("href")
    with open("links.txt", "a") as f:
        f.write(str(a_link)+"\n")

time.sleep(5)
driver.quit()
