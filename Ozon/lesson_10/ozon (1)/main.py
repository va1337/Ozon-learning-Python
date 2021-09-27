from functools import reduce
import random
import time


#1 2 3 4 5 6 7

# 1 Функциональный стиль который увеличивает все значения на 1 (map)
print(list(map(lambda x: int(x)+1, input().split())))


#2 Функциональный стиль c фильтрацией больше 5 (filter)
print(list(filter(lambda x: int(x) > 5, input().split())))


#3 Функциональный стиль c суммой всех чисел (reduce)
print(reduce(lambda x,y: int(x)+int(y), input().split()))


#4 Функциональный стиль (zip)

a = list(range(5))

b = 'abcde'

c = ['x','y']

print(list(zip(a,b,c)))


print(reduce(lambda x,y: x+y,list(filter(lambda x: x > 5,list(map(lambda x: int(x)+1, input().split()))))))


## Тут пример с kwargs и args
def func_kwargs(**kwargs):
    for k,v in kwargs.items():
        print(k,'-',v)


def func_args(*args):
    for i in args:
        print(i)


func_kwargs(firstname='Petr', surname='Urkovskiy', age=5)

func_args(1,2,3,4,5,6,76)


# Пример как можно все сломать от одной запятой  (a+1,)
def func(a,b):

    l = a + 1,
    print(l)
    return b + l # 2 + (2,) -> 2 + [2]

print(func(a=1,b=2)) 





def time_of_func(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print('Время функции', time.time() - start)
        return result
    return wrapper



@time_of_func
def bubble_sort(input_list):
    for iter_num in range(len(input_list) - 1, 0, -1):
        for i in range(iter_num):
            if input_list[i] < input_list[i + 1]:
                temp = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = temp



def quicksort(alist, end, start=0):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)
 
 
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j





@time_of_func
def start_quicksort(*args):
    return quicksort(*args)

a = [random.randint(1,10) for i in range(100000)]


start_quicksort(a, len(a))


a = [random.randint(1,10) for i in range(100000)]


bubble_sort(a)


def func_cre2(func):
    def func_c():
        return func() + '->'
        
    return func_c


def func_cre(func):
    return func()*2


@func_cre2
def func():
    return 'hello'*3



#a = func_cre(func)

#print(a)

a = func_cre2(func)()

a = func()

print(a)


