# Задание №2
class Person:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return(f'{self.name} {self.surname}')

class Student(Person):
    def __init__(self, surname, name, group_number, marks):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.marks = marks

    def set_test_score(self, mark):
        self.mark = mark
        self.marks.append(mark)

    def __str__(self):
        return (f'Студент {self.name} {self.surname}, группа {self.group_number}, оценки {self.marks}')

shkola = Student(name = 'Anton', surname = 'Antonov', group_number = '337', marks = [3,3,7])
print(shkola)
shkola.set_test_score(4)
print(shkola)