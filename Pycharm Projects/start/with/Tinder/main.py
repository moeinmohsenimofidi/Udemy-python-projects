from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROIMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/Users/Moien/development/chromedriver.exe"

TWITTER_PASSWORD = "moien12345"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        accept = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(1)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button").click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"upload = {self.up}\n downlaod = {self.down}")

    def tweet_at_provider(self):

        log_in_page = self.driver.get("https://twitter.com/i/flow/login")

        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        email.send_keys("seyedmoeinmohsenimofidi@gmail.com")
        time.sleep(3)
        email.send_keys(Keys.ENTER)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
#bot.get_internet_speed()
bot.tweet_at_provider()












