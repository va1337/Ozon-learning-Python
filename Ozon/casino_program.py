from random import randint
print('Добро пожаловать! На ваш депозит начислено 10000!')
deposit = 10000
while deposit != 0:
        print(f'Ваш депозит равен {deposit}')
        throw = randint(2,13)
        choice = int(input('Угадайте число (от 1 до 12) ! Если угадаете - выиграете 1000. В противном случае, '
                           'вы проиграете 1000'))
        while choice < 2 or choice > 12:
            choice = int(input('Введите число от 2 до 12:'))
        print(f'Вы загадали {choice}. В этот раз выпало {throw}')
        if choice == throw:
            deposit += 1000
        else:
            deposit -=1000

print('Вы проиграли, игра окончена!')

