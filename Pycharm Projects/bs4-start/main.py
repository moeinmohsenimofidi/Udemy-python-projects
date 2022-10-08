from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:

    text = article_tag.get_text()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)
largest_number = max(article_upvotes)
largest_number_index = article_upvotes.index(largest_number)
print(f"article:{article_texts[largest_number_index]}\nlink:{article_links[largest_number_index]}")































#with open("website.html", encoding="utf8") as file:
#    contents = file.read()
#
#soup = BeautifulSoup(contents, "html.parser")
#all_anchor_tags = soup.find_all(name="a")
#
#for tag in all_anchor_tags:
#    print(tag.getText(#))
#