#Задание №4
import requests
from bs4 import BeautifulSoup
import re
# Ссылка на наш источник парсинга

url = 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D1%8C%D1%8E%D0%BB%D0%B0'

# запрос в steam
resp = requests.get(url).text

# Создание объекта для париснга html
soup = BeautifulSoup(resp, 'html.parser')
str_to_detect = 'wikipedia'
for el in soup.find_all('a'):
    if (re.search(str_to_detect, str(el.get('href'))) == None) == True:
        if len(re.findall('https?', str(el))) > 0:
            print(el.get('href'))