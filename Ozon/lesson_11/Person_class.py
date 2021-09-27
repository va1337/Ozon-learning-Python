# Задание №1
class Person:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return(f'{self.name} {self.surname}')

chelik = Person(
    name = 'Иван',
    surname = 'Иванов'
)

chel2 = Person(
    surname = 'Kozlov',
    name = 'Vladislav'
)
print(chelik)
print(chel2)