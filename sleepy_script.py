import time
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

def take_time():
	hours = int(input("Enter the hours : "))
	mins = int(input("Enter the minutes : "))
	seconds = int(input("Enter the seconds : "))
	total_time = hours*60*60 + mins*60 + seconds
	return total_time

def websites():
	print("Your website list : ")
	print("1. Google (https://www.google.com)")
	print("2. Facebook (https://www.facebook.com/)")
	print("3. Netflix (https://www.netflix.com/in/)")

print()
print("WELCOME TO AUTO-BROWSE")
print()
websites()
print()

choice = int(input("Enter the choice : (-1 to specify other) : "))
if (choice == 1):
	website = "https://www.google.com"
elif (choice == 2):
	website = "https://www.facebook.com/"
elif (choice == 3):
	website = "https://www.netflix.com/in/"
else:
	website = input("Enter the website URL : ")

#creating service worker
serv = Service("/home/kartik/Downloads/Drivers/geckodriver")
driver = webdriver.Firefox(service = serv)
driver.get(website)

print()
print("\t\tTIME SCRIPT")
print()
localtime = time.localtime()
result = time.strftime("Current time : %I:%M:%S %p", localtime)
print(result)
print()
print("Enter the action :")
print("1. Shutdown")
print("2. Restart")
print("3. Lock")
print()

while True:
	choice = int(input("Enter the choice : "))	
	if (choice not in [1,2,3]):
		print("Please enter the correct choice!")
		print()
	else:
		if (choice == 1):
			print("Enter after how much time you want your system to shutdown :")
			total_time = take_time()
			print()
			print("Timer set for shutdown")
			time.sleep(total_time)
			driver.quit()
			print("Going to shutdown the system after 5 seconds")
			time.sleep(5)
			print()
			subprocess.run(["shutdown", "-h", "0"])
			break
		elif (choice == 2):
			print("Enter after how much time you want your system to restart :")
			total_time = take_time()
			print()
			print("Timer set for restart")
			time.sleep(total_time)
			driver.quit()
			print("Going to restart the system after 5 seconds")
			print()
			time.sleep(5)
			subprocess.run(["reboot"])
		else:
			print("Enter after how much time you want your system to lock :")
			total_time = take_time()
			print()
			print("Timer set for lock")
			time.sleep(total_time)
			driver.quit()
			print("Going to lock the system after 5 seconds")
			print()
			time.sleep(5)
			subprocess.run(["gnome-screensaver-command","-l"])
			break
