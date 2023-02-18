from twilio.rest import Client

TWILIO_SID = "AC08622509b57a5b740fc436582cb6dfdc"
TWILIO_AUTH_TOKEN = "63b87758758ba53d55906a0cffbb78eb"
TWILIO_VIRTUAL_NUMBER = '+13023033005'
TWILIO_VERIFIED_NUMBER = '+37368049431'


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
