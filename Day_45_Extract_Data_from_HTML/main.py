from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
#print(yc_web_page)
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="??????")
# print(articles)

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)

print(article_texts)
print(article_links)












# #import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title)
# #print(soup.title.string)
# #print(soup.prettify())
# #print(soup.a) # find first anchor tag
# all_anchor_tags = soup.find_all(name="a") # find all anchor tags
#
# for tag in all_anchor_tags: # search tags
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# selection_heading = soup.find(name="h3", class_="heading") # you need to name class using _
# print(selection_heading.string)
#
# company_url = soup.select_one(selector="p a")
# print (company_url)
# headings = soup.select(".heading")
# print(headings)
