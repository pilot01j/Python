from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Developement\chromedriver.exe"
driver_path = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_path)
import time

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
for x in range (100):
    cookie.click()

#time.sleep(15)