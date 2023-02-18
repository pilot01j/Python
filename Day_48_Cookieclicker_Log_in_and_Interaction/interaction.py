from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Developement\chromedriver.exe"
driver_path = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_path)
import time

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(articles.text)
#articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Third Punic War")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(5)