import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

GENDER = "male"
WEIGHT_KG = 120.4
HEIGHT_CM = 183.6
AGE = 34

APP_ID = "0401a38c"
API_KEY = "e21174980b5cf830cad3a34cf02e5edf"
USERNAME = "moien3m"
PASSWORD = "moien8981"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ff3c1dac703912f23939edb143dbfd82/workoutTracking/workouts"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": "Basic bW9pZW4zbTptb2llbjg5ODE="
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today = datetime.now().strftime("%Y%m%d")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
#sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#print(sheet_response.text)

sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(USERNAME, PASSWORD),
  headers=headers
)