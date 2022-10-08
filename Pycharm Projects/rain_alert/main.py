import requests
from twilio.rest import Client
api_key = "76649ade2d54e33b186477566df8363f "
endpoint = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = "AC61f044e23d96a1674b8a6bab28fc41f5"
auth_tiken = "6b7767588eefaae789bb8e80eb3f3989"

parameters = {
    "lat": 46.496719,
    "lon": 11.358000,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
will_rain = False

response = requests.get(endpoint, params=parameters)
print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data  in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)< 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_tiken)
    message = client.messages.create(
        body="It is going to rain today,do not forget to bring your umbrella",
        from_=,
        to=
    )
    print(message.status)
