from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


CHROME_DRIVER_PATH = "C:/Users/Moien/development/chromedriver.exe"
TARGET_ACCOUNT = "chefsteps"
USERNAME = "seyedmoeinmohsenimofidi@gmail.com"
PASSWORD = "moien8981@"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):


        self.driver.get("https://www.instagram.com/")
        time.sleep(1)
        allow = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[2]").click()
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        username.send_keys(USERNAME, Keys.TAB)
        password = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(2)

    def find_followers(self):
        time.sleep(2)
        self.driver.get(F"https://www.instagram.com/{TARGET_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element(By.CSS_SELECTOR, "._aa_5 a")
        followers.click()
        time.sleep(2)


    def follow(self):

        all_buttons = self.driver.find_element(By.CSS_SELECTOR, "._acan _acap _acas div button")
        for button in all_buttons:
            #button.click()
            #time.sleep(2)
            #try:
            #    button.click()
            #    time.sleep(2)
            #except ElementClickInterceptedException:
            #except ElementClickInterceptedException:
                #cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                #cancel_button.click()



bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()




