while True:
    try:
        birthday_year = int(input('Введите ваш год рождения:'))
        while birthday_year < 0:
            birthday_year = int(input('Введите ваш год рождения(положительное значение):'))
        print(birthday_year)
        break
    except ValueError:
        print('Ошибка, введите число!')
while True:
    try:
        count_year = int(input('Введите год, к которому нужно рассчитать ваш возраст:'))
        while count_year < birthday_year:
            count_year = int(input('Введите год, к которому нужно рассчитать ваш возраст (должен быть больше вашего года рождения):'))
        print(count_year-birthday_year)
        break
    except ValueError:
        print('Ошибка, введите число!')
