from bs4 import BeautifulSoup
import requests

BASE_URL = "https://vjdwzm.api.infobip.com"
API_KEY = "App eeb9f5c7b6cdbabbc8b7551bdca15e34-fc0e9c9e-64d2-4d54-ae0c-685e34ed8922"

SENDER_EMAIL = "pilot01j@selfserviceib.com"
RECIPIENT_EMAIL = "pilot01j@gmail.com"
EMAIL_SUBJECT = "Amazon Price Alert!"
EMAIL_TEXT = "The Kindle Oasis price now is: $"

URL = "https://www.amazon.com/All-new-Essentials-including-Graphite-Amazon/dp/B07RQNBBL8/ref=sr_1_13?keywords=" \
      "Kindle+E-readers&pd_rd_r=6082b290-4ed7-4976-bada-376dbc8515f1&pd_rd_w=liDpI&pd_rd_wg=7Whv6&pf_rd_p=b9deb6fa-" \
      "f7f0-4f9b-bfa0-824f28f79589&pf_rd_r=P1587JTBVZ0QDZHJVN89&qid=1673254125&sr=8-13"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ro;q=0.8,ro-MD;q=0.7,ru-MD;q=0.6,ru;q=0.5,ro-RO;q=0.4,de;q=0.3"
}
# Catch price

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(name="table", class_="a-lineitem a-align-top").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float <= 200:
    fromData = {
        "from": SENDER_EMAIL,
        "to": RECIPIENT_EMAIL,
        "subject": EMAIL_SUBJECT,
        "text": EMAIL_TEXT + f"{price_as_float}\n{URL}"
    }
    all_headers = {
        "Authorization": API_KEY
    }
    response = requests.post(BASE_URL + "/email/2/send", files=fromData, headers=all_headers)
    print("Status Code: " + str(response.status_code))
    print(response.json())
