#Задание №3
import re
file = open('lesson09_cats_of_ulthar.txt', 'r')
counter = 0
for line in file:
    #print(re.findall('[К,к]ошк\w+',line))
    counter += len(re.findall('[К,к]ошк\w+',line))
print(counter)