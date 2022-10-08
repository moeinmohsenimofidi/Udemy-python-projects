from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "C:/Users/Moien/development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in event_times:
   print(time.text)
event_subjects = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for subject in event_subjects:
   print(subject.text)
event = {}

for n in range(len(event_times)):
    event[n] = {
        "date": event_times[n].text,
        "subject": event_subjects[n].text,
    }
print(event)



