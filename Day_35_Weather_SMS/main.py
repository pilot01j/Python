
from twilio.rest import Client
import os
import requests

MY_LATITUDE = "47.010452"
MY_LONGITUDE = "28.863810"
api_id = "7dcf65e581b0c54179e0f85349ca3566"
account_sid = "AC08622509b57a5b740fc436582cb6dfdc"
auth_token = "63b87758758ba53d55906a0cffbb78eb"


weather_params = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_id
}

meteo_res = requests.get(
    url='https://api.openweathermap.org/data/2.5/forecast',
    params=weather_params
)
meteo_res.raise_for_status()
meteo_json = meteo_res.json()

will_rain = True
for hour_data in meteo_json:
    condition_code = meteo_json["list"][0]["weather"][0]["id"]
    #print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if not will_rain:
    pass
else:
    print("Bring an umbrella.")

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to 🌧️ today. Remember to bring an ☔. ",
        from_='+13023033005',
        to='+37368049431'
    )
print(message.status)