from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:/Users/Moien/development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
#driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")
#article_num = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#print(article_num.text)

#log_in = driver.find_element(By.LINK_TEXT, "Log in")
#log_in.click()

#search = driver.find_element(By.NAME, "search")
#search.send_keys("python")
#search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("moein")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("mohsenimofidi")
email = driver.find_element(By.NAME, "email")
email.send_keys("moein.mmofidi88@gmail.com")
submit = driver.find_element(By.XPATH, "/html/body/form/button")
submit.send_keys(Keys.ENTER)
