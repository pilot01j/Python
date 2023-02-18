from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
# xpath = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(xpath.text)

event_times = driver.find_element(By.CSS_SELECTOR, ".blog-widget time")
for time in event_times:
    print(time.text)
#driver.close()
driver.quit()