import requests

SHEET_ENDPOINT = "https://api.sheety.co/ff3c1dac703912f23939edb143dbfd82/flightDeals/users"
TEQUILA_API_KEY = "qTFtVn_0V9n6Rfk_bVrl0bslZBFYuOvE"

print("Welcome to Moein's Flight Club.\nWe find the best flight deals and email you.")
parameters = {
    "First Name": input("What is your firs name?\n").capitalize,
    "Last Name": input("What is your last name?\n").capitalize,
    "Email": input("What is your Email?\n")
}
headers = {
    "apikey": TEQUILA_API_KEY
}
confirmed_email = input("Write your Email again.\n")
# if confirmed_email == parameters["Email"]:
print("your Email has been added!!")
respond = requests.post(SHEET_ENDPOINT, params=parameters, headers=headersd )
print(respond.raise_for_status)
data = respond.json()
print(data)
