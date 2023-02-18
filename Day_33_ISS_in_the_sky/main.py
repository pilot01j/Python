import requests
from datetime import datetime
import time
from twilio.rest import Client

MY_LATITUDE = 47.060364
MY_LONGITUDE = 28.869841

BASE_URL = "https://vjdwzm.api.infobip.com"
API_KEY = "App eeb9f5c7b6cdbabbc8b7551bdca15e34-fc0e9c9e-64d2-4d54-ae0c-685e34ed8922"

account_sid = "AC08622509b57a5b740fc436582cb6dfdc"
auth_token = "63b87758758ba53d55906a0cffbb78eb"

SENDER_EMAIL = "pilot01j@selfserviceib.com"
RECIPIENT_EMAIL = "pilot01j@gmail.com"
EMAIL_SUBJECT = "Look ☝!"
EMAIL_TEXT = "The 🛰️ is above you in the sky."


def iss_is_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position = (iss_latitude, iss_latitude)
    print("ISS position:", iss_position)
    print("My position:", MY_LONGITUDE, MY_LATITUDE)
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE <= iss_longitude <= MY_LONGITUDE:
        return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }
    night_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    night_response.raise_for_status()
    data = night_response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    print("Time:", datetime.now(), "\n")
    if sunset + 2 <= time_now <= sunrise - 7:
        return True


def is_cloudy():
    querystring = {
        "lat": MY_LATITUDE,
        "lon": MY_LONGITUDE}

    headers = {
        "X-RapidAPI-Key": "a4acf5cc60mshedf448cb6050fbap1251c1jsn5be664799584",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    meteo_response = requests.get(
        url="https://weatherbit-v1-mashape.p.rapidapi.com/current",
        headers=headers,
        params=querystring)
    clouds_data = meteo_response.json()
    clouds = int(clouds_data["data"][0]["clouds"])
    if clouds <= 50:
        return True


is_true = True

while is_true:
    time.sleep(0.1)
    if iss_is_overhead() and is_cloudy() and is_night():
        # ---------------------SEND EMAIL---------------------- #
        formData = {
            "from": SENDER_EMAIL,
            "to": RECIPIENT_EMAIL,
            "subject": EMAIL_SUBJECT,
            "text": EMAIL_TEXT
        }
        all_headers = {
            "Authorization": API_KEY
        }
        response = requests.post(BASE_URL + "/email/2/send", files=formData, headers=all_headers)
        print("Status Code: " + str(response.status_code))
        print(response.json())

        # ---------------------SEND SMS---------------------- #
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{EMAIL_SUBJECT} {EMAIL_TEXT} ",
            from_='+13023033005',
            to='+37368049431'
        )
        print(message.status)
        is_true = False
