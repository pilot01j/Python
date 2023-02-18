from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Developement\chromedriver.exe"
driver_path = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_path)


driver.get("https://www.instagram.com/")
username = driver.find_element(By.NAME, "username")
username.send_keys("perfectlanguageschool")
password = driver.find_element(By.NAME, "password")
password.send_keys("perfectschool")
password.send_keys(Keys.ENTER)

time.sleep(15)