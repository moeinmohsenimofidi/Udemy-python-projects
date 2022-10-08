import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 200.0

URL = "https://www.amazon.com/SAMSUNG-Computer-Border-Less-FreeSync-LS24R350FZNXZA/dp/B091BCRJR7/ref=sr_1_12?keywords=24%2Binch%2Bmonitor&qid=1662711162&s=computers-intl-ship&sprefix=24%2Binch%2B%2Ccomputers-intl-ship%2C181&sr=1-12&th=1"
ACCEPT_LANGUAGE = "en-US,en;q=0.5"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"

MY_EMAIL = "seyedmoeinmohsenimofidi@yahoo.com"
MY_PASSWORD = "moien8981@"

HEADERS = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT,
}

response = requests.get(url=URL, headers=HEADERS)
html_web_page = response.text
soup = BeautifulSoup(html_web_page, "html.parser")
#print(soup.prettify())

price_full_format = soup.find(name="span", class_="a-price-whole").get_text()
price = float(price_full_format.split(".")[0])

title = soup.find(id="productTitle").get_text().strip()

if price < BUY_PRICE:
    message = f"{title}\n Is now available in ${price}"
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="moien.mmofidi88@gmail.com",
            msg=f"subject:🔥🔥🔥Amazon Price Alert🔥🔥🔥🔥 \n\n {message}\n For order this product you can use below URL:\n {URL}"
        )
