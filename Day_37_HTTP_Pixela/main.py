import requests
from datetime import datetime

USERNAME = "pilot01j"
TOKEN = "Maib4848@"
GRAPH_ID = "graph1"
url_pixela_endpoint = "https://pixe.la//v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# ----------------- Create Account on Pixela ---------------- #
# response = requests.post(url=url_pixela_endpoint, json=user_params)
# print(response.text)

# ----------------- Create Graphs on Pixela ---------------- #
url_graph_endpoint = f"{url_pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=url_graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
# my_graph_url = "https://pixe.la//v1/users/pilot01j/graphs/graph1.html"

url_pixel_creation_endpoint = f"{url_pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#today = datetime(year=2022, month=11, day=22)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "19.74",
}

# response = requests.post(url=url_pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


update_endpoint = f"{url_pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "-45.5"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)


# delete_endpoint = f"{url_pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

