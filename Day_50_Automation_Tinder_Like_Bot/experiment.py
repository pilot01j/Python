from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep


chrome_driver_path = "C:\Developement\chromedriver.exe"
driver_path = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_path)

# Click Login
driver.get("https://tinder.com/app/recs")
sleep(3)

driver.find_element(by=By.XPATH, value='//*[@id="c-1804602209"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
sleep(3)

# Click Facebook Login, will open Facebook popup login
driver.find_element(by=By.XPATH, value='//*[@id="c761984011"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()

# Switch to Facebook window & log in
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

driver.find_element(by=By.ID, value="email").send_keys("mucuta@yahoo.com")
driver.find_element(by=By.ID, value="pass").send_keys("Tekwill4848%")
driver.find_element(by=By.ID, value="pass").send_keys(Keys.ENTER)

# Allow for time to put in the 2-factor authorization code
sleep(20)

# Switch to Tinder window and dismiss all buttons
driver.switch_to.window(tinder_window)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="c761984011"]/div/div/div/div/div[3]/button[1]').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="c761984011"]/div/div/div/div/div[3]/button[2]').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="c-1804602209"]/div/div[2]/div/div/div[1]/div[1]/button').click()

# Let profiles load up and hit like. If no profile found, pass
sleep(20)

for n in range(10):
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