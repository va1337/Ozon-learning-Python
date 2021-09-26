#Задание №2
import re
list_of_galactics = []
file = open('lesson09_closest_galaxies.txt', 'r', encoding='utf-8')
for line in file:
    if (re.search('[А,а]ндромед',line.split(',')[0]) != None
        or re.search('[А,а]ндромед',line.split(',')[3]) != None)\
        and re.search('[0-9]',line.split(',')[2]) != None:
            list_of_galactics.append({'Название': line.split(',')[0], 'Расстояние' : float(line.split(',')[2][0:4]), 'Примечания': line.split(',')[3]})

newlist = sorted(list_of_galactics, key=lambda k: k['Расстояние'])
print(newlist)