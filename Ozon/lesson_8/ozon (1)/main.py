import requests
from bs4 import BeautifulSoup
import pprint
import random

#Ссылка на наш источник парсинга
url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

#запрос в steam
resp = requests.get(url).text

#Создание объекта для париснга html
soup = BeautifulSoup(resp, 'html.parser')

els = {}
els_a = {}
els_img = {}
names = []
#делаем цикл по всем элементам где найдем тэг "a" классом tab_item
for el in soup.find_all('a', class_='tab_item'):
    #делаем цикл по всем элементам где найдем тэг "div" классом tab_item_content
    for el_item in el.find_all('div', class_='tab_item_content'):
        #забираем текст имя по тэгу div с классом tab_item_name
        name = el_item.find('div', class_='tab_item_name').text
    tag = []
    for el_details in el.find_all('span', class_='top_tag'):
        tag.append(el_details.text)
    for el_details in el.find_all('div', class_='tab_item_cap'):
        img = el_details.find_all('img')[0]['src']
    els[name] = [x.replace(',','').strip() for x in tag]
    els_img[name] = img
    els_a[name] = el['href']
    names.append(name)

name = random.choice(names)

print(name)
print(els[name])
print(els_a[name])
print(els_img[name])