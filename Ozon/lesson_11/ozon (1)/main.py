

class User:
    def __init__(self, name, rang):
        self.name = name
        self.rang = rang

    def get_name(self):
        return self.name

    def talk(self):
        return 'Драться'
    
    def __str__(self):
        return f'{self.name} - {self.rang}'


class Orks(User):
    
    def __str__(self):
        return 'Арррр'



obj1 = User('Альясн', 80)


obj2 = Orks('Бохроман', 120)



print(obj1)

print(obj2)

print(obj2.talk())


print(obj1.talk())


print(obj1.get_name())




print(dir(obj1))