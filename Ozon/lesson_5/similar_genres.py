#Задание №1
anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}


def genres_intersepts(person1, person2):
    genres_for_both = set(person1.values()) & set(person2.values())
    if len(genres_for_both) == 0:
        return 'Общих жанров нет'
    else:
        genres_for_both = ', '.join(genres_for_both)
        return genres_for_both


print(genres_intersepts(anya, nastya))
print(genres_intersepts(olya, sveta))
print(genres_intersepts(sveta, anya))