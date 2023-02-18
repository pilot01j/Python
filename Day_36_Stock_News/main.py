import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_KEY = "IOXWIH8XJQB58O7V"

NEWS_URL = "https://newsapi.org/v2/top-headlines"
NEWS_KEY = "33d97a5023e24a25b61e2c125408ff3f"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "AC08622509b57a5b740fc436582cb6dfdc"
auth_token = "63b87758758ba53d55906a0cffbb78eb"

stock_parameters = {"function": "TIME_SERIES_DAILY_ADJUSTED",
                    "symbol": STOCK_NAME,
                    "apikey": ALPHAVANTAGE_KEY
                    }

news_parameters = dict(q=COMPANY_NAME, apikey=NEWS_KEY)


def get_stock_price():
    response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_stock_price = float(data_list[0]["4. close"])
    day_before_yesterday_stock_price = float(data_list[1]["4. close"])

    print(f"Yesterday stock price:", yesterday_stock_price,
          f"\nDay before yesterday stock price:", day_before_yesterday_stock_price)
    difference = yesterday_stock_price - day_before_yesterday_stock_price
    print("Diference:", difference, ";")
    return difference


def get_news():
    response = requests.get(url=NEWS_URL, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    main_news = []
    news_number = int(data['totalResults'])
    for x in range(news_number):
        if x >= 3:
            break
        else:
            main_news.append(f"{x + 1}. " + data["articles"][x]["title"] + ".")
    # print(main_news)
    return main_news


def send_message():
    client = Client(account_sid, auth_token)
    result = '\n'.join(get_news())
    text_msg = f"\n{result}"

    if 0 > get_stock_price() >= 5:
        dif = f"TSLA:  {get_stock_price()} 💲"
    else:
        dif = f"TSLA: 🔻 {get_stock_price()} 💲"
    message = client.messages.create(
        from_='+13023033005',
        body=f"{dif} {text_msg} ",
        to='+37368049431'
    )
    print(message.status)


send_message()
