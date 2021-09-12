#Задание №4
import time

dnevnik = open('dnevnik_log.txt', 'a')
print('Введите дату (dd/mm/yyyy):')
while True:
    try:
        date_write = input()
        valid_date = time.strptime(date_write, '%d/%m/%Y')
        break
    except ValueError:
      print('Неправильный формат!')
print('Введите информацию, которую хотите зафиксировать:')
info_write = input()
dnevnik.write(date_write + ' - ' + info_write + '\n')
dnevnik.close()
dnevnik = open('dnevnik_log.txt', 'r')
for line in dnevnik:
    print(line)
dnevnik.close()