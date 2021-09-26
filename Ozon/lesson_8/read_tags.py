# Задание №2
import requests
from bs4 import BeautifulSoup

# Ссылка на наш источник парсинга
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

# запрос в steam
resp = requests.get(url).text

# Создание объекта для париснга html
soup = BeautifulSoup(resp, 'html.parser')

tags_dict = {}
tags_names = []
tags_numbers = []
for el in soup.find_all('a', class_='btnv6_blue_hoverfade btn_small_tall'):
    for tag_info in el.find_all('span', class_='tag_name'):
        tags_names.append(tag_info.text)
    for tag_numbers in el.find_all('span', class_='tag_count tab_filter_control_count'):
        tags_numbers.append(tag_numbers.text.replace(',', ''))
for i in range(len(tags_names)):
    tags_dict[tags_names[i]] = tags_numbers[i]
print(tags_dict)