import requests
from twilio.rest import Client

account_sid = "AC61f044e23d96a1674b8a6bab28fc41f5"
auth_token = "6b7767588eefaae789bb8e80eb3f3989"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API = "a3c64417912c4e8f95f7428e42b4fdba"
STOCK_API_KEY = "8I361IXRPUG83ZIS"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_parameters = {
    "apikey": NEWS_API,
    "qInTitle": COMPANY_NAME,
}
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
print(response.raise_for_status)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
print(yesterday_closing_price)

day_before_yesterday_price = float(data_list[1]["4. close"])
print(day_before_yesterday_price)
difference = round(abs(yesterday_closing_price - day_before_yesterday_price), 2) / 100

difference_percentage = (difference / yesterday_closing_price) *100
print(difference_percentage)
if difference_percentage > 0:


    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    print(news_response.raise_for_status)
    three_articles = news_response.json()["articles"][:3]




formatted_articles = [f"Headlines : {article['title']}.\n Brief: {article['description']}"for article in three_articles]



client = Client(account_sid, auth_token)

message= client.messages.create(
    body= f"Tesla : {difference} % \n {formatted_articles}",
    from_=,
    to="+393313477856";
)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

