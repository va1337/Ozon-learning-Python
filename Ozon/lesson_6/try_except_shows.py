# Задание №1
shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
         'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
         'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98},
         'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
         'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87}, 'Карточный домик': {'Genre': 'драма',
                                                                                     'Rating': 0.82},
         'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}

ratings = []
for i in range(len(list(shows.values()))):
    ratings.append(list(list(shows.values())[i].values())[1])
try:
    print(sum(ratings) / len(ratings))
except TypeError:
    ratings = [float(i) for i in ratings]
    print(round(sum(ratings) / len(ratings), 2));
