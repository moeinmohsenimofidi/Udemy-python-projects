import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
header = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
}
CHROME_DRIVER_PATH = "C:/Users/Moien/development/chromedriver.exe"


DOC_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdAsRYOJXWkGNLLTjJ2FoH7hW6ARTppKyhPrFY8x2hgdgIcrg/viewform?usp=sf_link"

response = requests.get(ZILLOW_URL, headers=header)
zillow_web = response.text
soup = BeautifulSoup(zillow_web, "html.parser")

all_link_elements = soup.select('.StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 kJFQQX span')
for link in all_link_elements:
    print(link.text)
#all_links = []
#for link in all_link_elements:
#    href = link["href"]
#    print(href)
#    if "http" not in href:
#        all_links.append(f"https://www.zillow.com{href}")
#    else:
#        all_links.append(href)
#print(all_links)
#




