# Задание №4
import random, time
def selection_sort(input_list):
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time # время выполнения в секундах

def quicksort(nums):
   start_time = time.time()
   if len(nums) <= 1:
       return time.time() - start_time
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]

   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return time.time() - start_time


sizes = [1000, 2000, 5000, 10000]
for i in sizes:
    listik = [random.randrange(1, i*5, 1) for j in range(i)]
    print(f'Длина списка: {len(listik)}, время сортировки (выбором): {selection_sort(listik)}')
    print(f'Длина списка: {len(listik)}, время сортировки (быстрая): {selection_sort(listik)}')
    print('*'*20)
'''
Метод взят отсюда: https://gb.ru/posts/python_sort
Сортировки отрабатывают примерно одинаково. 
'''