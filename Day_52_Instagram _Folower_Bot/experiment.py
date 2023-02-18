from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException

DRIVER_PATH = Service('C:\Development\chromedriver.exe')
TARGET_USER = 'instagram'
USER_NAME = 'pilot02j@gmail.com'
PASSWORD = 'Maib4848@'
INSTA_URL = 'https://www.instagram.com/'


# create class and inside init create driver for browser
class InstagramFollowersBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.driver.maximize_window()

    def log_in(self, url):
        # browse to instagram.com
        self.driver.get(url)
        sleep(5)
        # enter username
        user_name = self.driver.find_element(By.NAME, 'username')
        user_name.send_keys(USER_NAME)
        # enter password
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        sleep(2)
        # click log in after entering user credentials
        click_log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        click_log_in.click()
        sleep(10)
        # click on Not now, if you don't want to save password.
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(5)
        # click on Not now, if you don't want to turn on notifications.
        self.driver.find_element(By.CSS_SELECTOR, '.mt3GC .HoLwm ').click()

    def find_followers(self, target_user):
        # enter username of the target person
        enter_name = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        enter_name.send_keys(target_user)
        sleep(3)
        # click on user that you searched
        self.driver.find_element(By.CSS_SELECTOR, '.fuqBx a').click()
        sleep(5)
        # click on followers, this will open followers pop up window
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section'
                                                       '/ul/li[2]/a/div')
        followers.click()
        sleep(5)
        # select the scrollable part of the popup window
        pop_up_window = self.driver.find_element(By.CLASS_NAME, 'isgrP')
        # scroll down to load more and more followers
        for i in range(5):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', pop_up_window)
            sleep(2)

    def follow(self):
        # create list of all the follower elements
        followers_list = self.driver.find_elements(By.CSS_SELECTOR, '#fc75366a8bc08 > button > div')
        # loop through each follower in follower list
        for follower in followers_list:
            try:
                follower.click()
                sleep(1)
            # if sometimes we click on following instead of follow, so instagram displays pop up to confirm unfollow
            except ElementClickInterceptedException:
                # click on cancel
                self.driver.find_element(By.CSS_SELECTOR, '#fc75366a8bc08 > button > div').click()
                sleep(2)

        # self.driver.quit()

            # another method, by checking if button == Follow than and only click on button otherwise leave
            # if follower.text == 'Follow':
            #     follower.click()
            #     sleep(1)
            # else:
            #     print('Already Following or requested')


bot = InstagramFollowersBot(DRIVER_PATH)
bot.log_in(INSTA_URL)
bot.find_followers(TARGET_USER)
bot.follow()