# Задание №1

import requests
from bs4 import BeautifulSoup


# Ссылка на наш источник парсинга
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

# запрос в steam
resp = requests.get(url).text

# Создание объекта для париснга html
soup = BeautifulSoup(resp, 'html.parser')

# 1.1

'''for el in soup.find_all():
    print(el)'''

# 1.2

'''for el in soup.find_all('a'):
    print(el.text)
    print(el.get('href'))'''

# 1.3

f2p_dict = {}
for el in soup.find_all('a', class_='tab_item'):
    if 'Free to Play' in el.text:
        f2p_dict[el.find('div', class_= 'tab_item_name').text] = el.get('href')
    else:
        pass
print(f2p_dict)