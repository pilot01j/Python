from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "C:\Developement\chromedriver.exe"
driver_path = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_path)

driver.get("https://www.linkedin.com/")
log_in = driver.find_element(By.NAME, "session_key")
log_in.click()
log_in.send_keys("marin.mucuta.it@gmail.com")
password = driver.find_element(By.NAME, "session_password")
password.send_keys("Maib4848")
log_in_button = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
log_in_button.send_keys(Keys.ENTER)
search_button = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search_button.send_keys("python developer")
search_button.send_keys(Keys.ENTER)
# job_link = driver.find_element()
# job_link.click()


time.sleep(55)
driver.quit()

