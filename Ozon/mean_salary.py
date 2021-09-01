'''
Версия №1 -
total_sum = 0
while True:
    try:
        salary1 = int(input('Введите ЗП первого члена семьи:'))
        salary2 = int(input('Введите ЗП второго члена семьи:'))
        salary3 = int(input('Введите ЗП третьего члена семьи:'))
        break
    except ValueError:
        print('На вход было подано не число, введите зарплаты заново!')
total_sum = salary1 + salary2 + salary3
print(total_sum / 3)

Хотел бы добавить возможность, чтобы если для 2 или 3 члена семьи введено не число, 
чтобы с него начиналось присваивание значения, а не заново с первого.
Но я не смог сходу придумать, как это красиво обернуть, а не тремя while try break except
'''

'''
Версия №2
Ввёл в гугле вопрос "custom amount of inputs python"
Можно еще добавить проверку на отрицательное значение n и зарплат в идеале.
'''

n = int(input('Введите количество членов семьи:'))
List = []  #declare an Empty list
for i in range(1, n+1):
    while True:
        try:
            elem = int(input('Введите ЗП '+ str(i) + ' члена семьи:'))
            List.append(elem)
            break
        except ValueError:
            print('На вход было подано не число, введите зарплату заново!')
print(sum(List) / len(List))