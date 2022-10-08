from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

EMAIL = "moien.mmofidi88@gmail.com"
Password = "moien8981@"
PHone_number = "3313477856"

chrome_driver_path = "C:/Users/Moien/development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3259906727&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

driver.maximize_window()
log_in = driver.find_element(By.LINK_TEXT, "Sign in").click()

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(Password)
password.send_keys(Keys.ENTER)

time.sleep(3)

easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button ")
easy_apply.click()

time.sleep(5)
fill_field = driver.find_element(By.CSS_SELECTOR, ".display-flex input")
fill_field.send_keys(PHone_number)

next = driver.find_element(By.CSS_SELECTOR, "footer button")
next.click()
time.sleep(2)
next.send_keys(Keys.ENTER)

field1 = driver.find_element(By.ID, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3259906727,67807962,numeric)")
field1.send_keys("1")
field2 = driver.find_element(By.ID, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3259906727,67808002,numeric)")
field2.send_keys("1")
field3 = driver.find_element(By.ID, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3259906727,67808010,numeric)")
field3.send_keys("1")
time.sleep(1)

review = driver.find_element(By.CSS_SELECTOR, ".artdeco-button artdeco-button--2 artdeco-button--primary ember-view footer button")
review.click()




