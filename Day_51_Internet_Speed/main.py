from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
URL = "https://www.speedtest.net/"
PROMISED_DOWN = "1000"
PROMISED_UP = "100"


class InternetSpeedTwitterBot:

    def __init__(self, chrome_path: str):
        ser = Service(chrome_path)
        self.driver = webdriver.Chrome(service=ser)
        self.down = 0
        self.up = 0
        self.ping = 0

    def get_internet_speed(self, url: str):
        self.driver.get(url)
        self.driver.find_element(By.CLASS_NAME, "js-start-test.test-mode-multi").click()
        while self.driver.current_url == url:
            pass
        self.ping = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                     'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                             'div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        self.driver.quit()
        print(f"Ping: {self.ping} ms")
        print(f"UP speed: {self.up} Mbps")
        print(f"Down speed: {self.down} Mbps")

    def tweet_at_proveder(self):
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when " \
                f"I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        print(tweet)


speedtest = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
speedtest.get_internet_speed(URL)
speedtest.tweet_at_proveder()
