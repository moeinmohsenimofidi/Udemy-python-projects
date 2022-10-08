import requests
#from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

}
response = requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()

#ata = response.json()
#unrise = data["results"]["sunrise"]
#unset = data["results"]["sunset"]
#rint(sunset)
