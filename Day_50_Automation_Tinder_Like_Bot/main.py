from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep

chrome_driver_path = "C:\Developement\chromedriver.exe"
driver_path = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_path)

driver.get("https://tinder.com/")
# i_accept = driver.find_element(By.LINK_TEXT, 'I accept')
# i_accept.click()
sleep(2)
accept_button = driver.find_element(By.XPATH, '//*[@id="o-1773584476"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()
sleep(2)
log_in_button = driver.find_element(By.XPATH, '//*[@id="o-1773584476"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()
sleep(2)
log_in_by_facebook = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
log_in_by_facebook.click()

#Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys("mucuta@yahoo.com")
password.send_keys("Tekwill4848%")
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(10)

#Allow location

allow_location_button = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div/div/div[3]/button[1]').click()

sleep(2)
# #Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div/div/div[3]/button[2]').click()
sleep(4)
close_darck_mode = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[2]/button').click()

for n in range(100):
    try:
        sleep(1)
        ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    except NoSuchElementException:
        sleep(2)
        print("not found")
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    else:
        print("like!")
        sleep(1)
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()


sleep(1112)
driver.quit()