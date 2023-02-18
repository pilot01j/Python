from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "rochii.la.comanda"
USERNAME = "pilot03j@gmail.com"
PASSWORD = "Maib4848@"
LOG_IN_URL = "https://www.instagram.com/accounts/login/"
INSTA_URL = "https://www.instagram.com/"



class InstaFollower:
    def __init__(self, chrome_path: str):
        ser = Service(chrome_path)
        self.driver = webdriver.Chrome(service=ser)

    def login(self, url: str, username: str, password: str):
        self.driver.get(url)
        sleep(2)
        insert_username = self.driver.find_element(By.NAME, "username")
        insert_username.send_keys(username)
        insert_password = self.driver.find_element(By.NAME, "password")
        insert_password.send_keys(password)
        insert_password.send_keys(Keys.ENTER)
        sleep(10)
        save_latter_button = self.driver.find_element(By.CSS_SELECTOR, '._ac8f button')
        save_latter_button.click()
        sleep(5)
        notice_latter_button = self.driver.find_element(By.CSS_SELECTOR, '._a9-z button')
        notice_latter_button.click()
        sleep(5)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"{INSTA_URL}{SIMILAR_ACCOUNT}/")
        sleep(7)
        follower_bottom = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/'
                                                             'div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')
        follower_number_text = follower_bottom.text

        follower_number = follower_number_text.replace('.', '')
        follower_number = int(follower_number.split(' ')[0])
        print("Followers Number:", f"{follower_number}")

        follower_bottom.click()
        sleep(5)

        for num in range(1, follower_number):

            try:
                follower_button = self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/div[2]/div/div/'
                                                                     f'div[1]/div/div[2]/div/div/div/div/div[2]/div/'
                                                                     f'div/div[2]/div[1]/div/div[{num}]/div[3]/button')
                follower_button.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]'
                                                                   '/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/'
                                                                   'div/div/div[3]/button[2]')
                cancel_button.click()
                sleep(1)

add_followers = InstaFollower(CHROME_DRIVER_PATH)
add_followers.login(LOG_IN_URL, USERNAME, PASSWORD)
add_followers.find_followers()