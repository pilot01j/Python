import requests
from datetime import datetime
import time

MY_LATITUDE = 47.060364
MY_LONGITUDE = 28.869841

BASE_URL = "https://vjdwzm.api.infobip.com"
API_KEY = "App eeb9f5c7b6cdbabbc8b7551bdca15e34-fc0e9c9e-64d2-4d54-ae0c-685e34ed8922"

SENDER_EMAIL = "pilot01j@selfserviceib.com"
RECIPIENT_EMAIL = "pilot01j@gmail.com"
EMAIL_SUBJECT = "Look Up!"
EMAIL_TEXT = "The ISS is above you in the sky."


def iss_is_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position = (iss_latitude, iss_latitude)
    print(iss_position)
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
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if sunset + 2 <= time_now <= sunrise - 2:
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
    #print(clouds_data)

is_cloudy()