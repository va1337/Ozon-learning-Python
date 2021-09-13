# Задание №2
shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
         'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
         'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98},
         'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
         'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87}, 'Карточный домик': {'Genre': 'драма',
                                                                                     'Rating': 0.82},
         'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}

import pickle
def megafunc(genre):
    import pickle
    films_dict = {}
    list_of_films_with_ratings = []
    ratings_nums = []

    for i in range(len(list(shows.values()))):
        if list(list(shows.values())[i].values())[0] == genre:
            list_of_films_with_ratings.append(list(shows.keys())[i])
            ratings_nums.append(float(list(list(shows.values())[i].values())[1]))
            films_dict[genre] = {'Количество фильмов': len(ratings_nums),
                                 'Средний рейтинг': (sum(ratings_nums) / len(ratings_nums)),
                                 'Список фильмов': list_of_films_with_ratings}

    print(f'Жанр: {genre}, Количество фильмов: {len(ratings_nums)}, Средний рейтинг: {(sum(ratings_nums) / len(ratings_nums))}')


    a_file =open ('data.dat', 'wb')
    pickle.dump(films_dict, a_file)
    a_file.close()


all_genres = []
for i in range(len(list(shows.values()))):
    all_genres.append(list(list(shows.values())[i].values())[0])
all_genres = list(set(all_genres))
for i in all_genres:
    megafunc(i)

a_file = open('data.dat', 'rb')
output = pickle.load(a_file)
print(output)