#Задание №4
import requests
from bs4 import BeautifulSoup
# Ссылка на наш источник парсинга

url = 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D1%8C%D1%8E%D0%BB%D0%B0'

# запрос в steam
resp = requests.get(url).text

# Создание объекта для париснга html
soup = BeautifulSoup(resp, 'html.parser')

for el in soup.find_all('a'):
    print(el.get('href'))