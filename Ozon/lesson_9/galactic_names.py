#Задание №1
import re

file = open('lesson09_closest_galaxies.txt', 'r', encoding='utf-8')
for line in file:
    if re.search('[А,а]ндромед',line.split(',')[0]) != None \
            or re.search('Пегас',line.split(',')[0]) != None \
            or re.search('Кит', line.split(',')[0]) != None \
            or re.search('^[а-яА-я]', line.split(',')[0]) != None\
            or re.search('\d$', line.split(',')[0]) != None:
        print(line.split(',')[0])

