import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7e0a749e8acf6f2f875b842d9fe94012/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/7e0a749e8acf6f2f875b842d9fe94012/flightClubUsers/users"


# This class is responsible for talking to the Google Sheet.

class DataManager:

    def __init__(self):
        self.users_data = None
        self.destination_data = {}

    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.users_data = data["users"]
        print(data)
        return self.users_data

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def create_account_flight_club(self):
        print("Welcome to Marin's Flight Club.\n"
              "We find the best flight deals and email you")
        user_first_name = input("What is your first name?\n")
        user_last_name = input("What is your last Name\n")
        user_email = input("What is your email?\n")
        confirm_email = input("Type your email again.\n")
        if user_email == confirm_email:
            new_data = {
                "user": {
                    "firstName": user_first_name,
                    "lastName": user_last_name,
                    "email": user_email,
                }
            }
            response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_data)
            print("response.status_code =", response.status_code)
            print("response.text =", response.text)
            print("You're in the club!")
        else:
            print("Lon in Fail - Please try again.")

    def delete_user_row(self):
        row_number = str(input("What row do you want to delete:\n"))
        response = requests.delete(url=f"{SHEETY_USERS_ENDPOINT}/{row_number}")
        print("response.status_code =", response.status_code)
        print(f"Row number {row_number} was successfully deleted.")
