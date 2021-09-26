# Задание №3
import requests
from bs4 import BeautifulSoup

# Ссылка на наш источник парсинга
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

# запрос в steam
resp = requests.get(url).text

# Создание объекта для париснга html
soup = BeautifulSoup(resp, 'html.parser')

games_with_tags = {}
for el in soup.find_all('div', class_='tab_content_ctn sub'):
    for game_info in el.find_all('div', class_='tab_item_content'):
        name = game_info.find('div', class_='tab_item_name').text
        tags = (game_info.find('div', class_= 'tab_item_top_tags').text).split()
        games_with_tags[name] = tags
print(games_with_tags)