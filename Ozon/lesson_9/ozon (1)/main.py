
import re
from text import text1,text2,text3,text4,text5


#1 Поиск по совпадениям


print(re.findall('[a-zA-Z]+', text1))
print(re.findall('[0-9]+', text1))


# YYYY-MM-DD
#
#Виды дат
# YYYY-MM-DD
#2021-03-22
#  DD/MM/YY
#. 10/11/06

# 10 ноября 2006
# Ноябрь 10, 2006

#YYYY-MM-DD
# строго 1 символ 1 или 2 а потом по формату 
print(re.findall('[1,2]{1}[0-9]{3}-[0-9]{2}-[0-9]{2}', text2))

# строго по формату
print(re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}', text2))

#MM/DD/YY
print(re.findall('[0-9]{2}/[0-9]{2}/[0-9]{2}', text2))


print(re.findall('[0-9]+ [a-zA-Z]+ [0-9]+', text2))


print(re.findall('\s"[a-zA-Z0-9\s\,]+"', text2))


#Шаблон для поиска
print(re.findall('ISO\s[0-9]+', text2))

#Шаблон для поиска слов кирилицей и латиницей
print(re.findall('[а-яёА-ЯЁ]+', text2))
print(re.findall('[a-zA-Z]+', text2))

print(re.findall('[A-Z][a-z]+', text2))# поиск слов с заглавной буквой



#2 РАЗДЕЛЕНИЕ ТЕКСТА
#Разделять текст по предложениям
words_struct = re.split('\.|\?|\!', text3)

for i in range(len(words_struct)):
    words_struct[i] = words_struct[i].strip()

for i in words_struct:
    print(i)
    

#Разделять текст по строкам
words_struct2 = re.split('\n', text2)
for i in words_struct2:
    print(i)




#3 ЗАМЕНА

words = re.sub('НЛО|[0-9]{4}|[А-Я][а-яё\s]+', 'XXXX', text4)

print(words)



words = re.sub('НЛО', 'Навальный', text4)

print(words)



import pymorphy2

morph = pymorphy2.MorphAnalyzer()
a = morph.parse('Навального')
print(a)





#4 Вычесление по неструктурированному тексту

videos = {
    'Video 1': '3ч 15мин',
    'Video 2': '1 час, 7 минут',
    'Video 3': '36мин',
    'Video 4': '2 часа',
}

result = {}

for k,v in videos.items():

    h_,m_ = 0,0

    h = re.search('([0-9]+)(\s)?ч', v)

    if h:
        h_ = h[0].split('ч')[0].split()[0]
    
    m = re.search('([0-9]+)(\s)?м', v)

    if m:
        m_ = m[0].split('м')[0].split()[0]
    

    result[k] = int(h_) * 60 + int(m_)


print(result)
