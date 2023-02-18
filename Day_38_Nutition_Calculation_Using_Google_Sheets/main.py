import requests
from datetime import datetime

APP_ID = "3f21ecbb"
API_KEY = "958270c527175cec44f94ed9c8e42c92"
USER_ID = "pilot01"
url_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 173
AGE = 30

user_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

params_url_nutritionix = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=url_nutritionix, json=params_url_nutritionix, headers=user_headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    SHEET_USERNAM = "pilot01j"
    SHEET_PASSWORD = "Maib4848@2022"
    url_sheet = "https://api.sheety.co/7e0a749e8acf6f2f875b842d9fe94012/myWorkouts/workouts"
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=url_sheet, json=sheet_inputs, auth=(SHEET_USERNAM, SHEET_PASSWORD))

    print(sheet_response.text)
