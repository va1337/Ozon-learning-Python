
#экземпляр класса == объект

class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday
    
    def __str__(self):
        return f'Привет, меня зовут {self.name}' 

    def print_contact(self):
        print(f'{self.name} живет в {self.address}')



leo = Contact(
    name='Лев Толстой',
    phone = '8800223535',
    address = 'Ясная Поляна',
    birthday = '09.09.1828'
)


harry = Contact(
    name='Гарри Поттер',
    phone = '123800223535',
    address = 'Лондон',
    birthday = '01.09.1996'
)


#print_contact(harry)
#print_contact(leo)

harry.print_contact()

leo.print_contact()