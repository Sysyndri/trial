import requests
from bs4 import BeautifulSoup
import json

# Парсинг цитат с первой страницы сайта
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, features='html.parser')

post = soup.find_all("div", class_="quote")

posts_one_str = dict()
for line in post:
    text = line.find('span').text
    author = line.find('small').text

    posts_one_str[author] = text


# Парсинг данных со страницы по тегу пользователя
post_user_tag = dict()

user_search_tag = input("Введите тег по которому хотите искать данные: ").lower()
tags = soup.find_all('div', class_='tags')
for line in post:
    text_tag = [s.text for s in line.find_all('a', class_="tag")]
    if user_search_tag in text_tag:
        text = line.find('span').text
        author = line.find('small').text

        post_user_tag[author] = text


post_str = json.dumps(posts_one_str, indent=4, ensure_ascii=False)
post_tag = json.dumps(post_user_tag, indent=4, ensure_ascii=False)

with open("post.json", 'w', encoding='UTF-8') as file:
    file.write(f"Посты с первой страницы сайта:\n{post_str}\n")
    file.write(f"Посты найденные по указанному тегу:\n{post_tag}\n")
