import requests
from twilio.rest import Client

TWILIO_SID = "AC08622509b57a5b740fc436582cb6dfdc"
TWILIO_AUTH_TOKEN = "63b87758758ba53d55906a0cffbb78eb"
TWILIO_VIRTUAL_NUMBER = '+13023033005'
TWILIO_VERIFIED_NUMBER = '+37368049431'

BASE_URL = "https://vjdwzm.api.infobip.com"
API_KEY = "App eeb9f5c7b6cdbabbc8b7551bdca15e34-fc0e9c9e-64d2-4d54-ae0c-685e34ed8922"

SENDER_EMAIL = "pilot01j@selfserviceib.com"
RECIPIENT_EMAIL = "pilot01j@gmail.com"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, ):
        formData = {
            "from": SENDER_EMAIL,
            "to": emails,
            "subject": "Chip Flights",
            "text": message
        }

        all_headers = {
            "Authorization": API_KEY
        }

        response = requests.post(BASE_URL + "/email/2/send", files=formData, headers=all_headers)
        print("Status Code: " + str(response.status_code))
        print(response.json())
