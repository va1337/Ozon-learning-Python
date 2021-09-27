'''
text = 'Война и Мир' #str

a = 1


class <Имя класса>:

    def __init__(self, <параметров конструктора>):
        тело метода
'''
import time

class Time:

    def __init__(self, seconds):
        self.hours = seconds // 3600
        seconds = seconds % 3600
        self.minutes = seconds // 60
        self.seconds = seconds % 60
        self.time = [self.hours, self.minutes, self.seconds]
    
    def __getitem__(self, i):
        return self.time[i]
    
    def __setitem__(self, i, value):
        self.time[i] = value

    def __iter__(self):
        for i in range(len(self.time)):
            yield self.time[i]
    
    def __call__(self):
        seconds = time.time()
        self.hours = seconds // 3600
        seconds = seconds % 3600
        self.minutes = seconds // 60
        self.seconds = seconds % 60
        return f'{self.hours} ч {self.minutes} м {self.seconds} c'

    def __len__(self):
        return (self.hours * 60 + self.minutes) * 60 + self.seconds
    
    def __add__(self, other):
        other_other = Time(len(self)+len(other))
        return other_other

    def __str__(self):
        return str((self.hours * 60 + self.minutes) * 60 + self.seconds)
        

one = Time(1234)

two = Time(4321)

print(one)

print(two)

new_obj = one+two+one+one+one+one

print(new_obj())