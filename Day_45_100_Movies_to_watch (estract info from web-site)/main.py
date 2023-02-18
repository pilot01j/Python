import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Extract info from webpage and create a list of best 100 movies
response = requests.get(url=URL)
yc_web_page = response.text
#print(yc_web_page)
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="h3", class_="title")
article_texts = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
reversed_article_texts = reversed(article_texts)
# print(article_texts)
# print(len(article_texts))

with open("movies.txt", "w", encoding="utf-8") as file:
    for item in reversed_article_texts:
        file.write(item+"\n")
