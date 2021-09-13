# Задание №3
import random, time
def selection_sort(input_list):
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time # время выполнения в секундах

sizes = [1000, 2000, 5000, 10000]
for i in sizes:
    listik = [random.randrange(1, i*5, 1) for j in range(i)]
    print(f'Длина списка: {len(listik)}, время сортировки: {selection_sort(listik)}')
'''
Чем больше длина списка, тем больше увеличение во времени
переход с 1000 до 2000 (кол-во строк увеличилось в 2 раза) занимает в 3 раза больше времени
переход с 2000 до 5000 (кол-во строк увеличилось в 2.5 раза) занимает 6.3 раза больше времени
переход с 5000 до 10000 (кол-во строк увеличилось в 2 раза) занимает 4 раза больше времени
И соответственно, переход с 1000 до 10000 (кол-во строк увеличилось в 10 раз) занимает 86 раза больше времени
Из-за сложности O(n^2) этот метод сортировки неприменим для большим объемов данных
'''

