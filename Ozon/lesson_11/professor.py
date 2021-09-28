# Задание №3
import random
class Person:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return(f'{self.name} {self.surname}')

class Student(Person):
    def __init__(self, surname, name, course_name, marks):
        self.surname = surname
        self.name = name
        self.course_name = course_name
        self.marks = marks

    def set_test_score(self, mark):
        self.mark = mark
        self.marks.append(mark)


class Professor(Person):
    def test_students(self, students_list):
        self.students_list = students_list
        for i in self.students_list:
            i.set_test_score(random.randint(0,11))

    def __str__(self):
        return (f'Преподаватель {self.name} {self.surname} читает курс ООП')


Grisha = Professor(name = 'Геогрий', surname= 'Симонов')
print(Grisha)


student1 = Student(surname='Антонов', name= 'Антон', course_name= 'ООП', marks= [])
student2 = Student(surname='Петров', name = 'Петр', course_name= 'Музыка', marks= [])
student3 = Student(surname='Иванов', name= 'Иван', course_name='Пение', marks= [])

studentiki = [student1, student2, student3]
Grisha.test_students(studentiki)
Grisha.test_students(studentiki)

print(student1.marks)
print(student2.marks)
print(student3.marks)