#Задание №3
string_to_find = 'кошка'
file1 = open('lesson05_cats_of_ulthar.txt', 'r')
counter = 0
for line in file1:
    if string_to_find in line:
        counter += 1
        print(line)
print(f'Слово "кошка" встретилось в тексте {counter} раз(а)')
file1.close()
