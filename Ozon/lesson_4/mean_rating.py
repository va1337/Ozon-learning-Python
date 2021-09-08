shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
'''
print([*shows])
print(shows.values())


for i in ratings: # отразить все фильмы
    print (i)
'''
#for i in ratings: # отразить все жанры
#    print (ratings[i])
ratings_list = []
fantasy_shows = dict(filter(lambda elem: elem[1] == 'фантастика', shows.items()))
for i in fantasy_shows:
    ratings_list.append(ratings[i])
print(sum(ratings_list) / len(ratings_list))
'''
ratings_numbers = list(ratings.values())
ratings_films = [k for k in shows.keys() if fantasy_shows.keys() in shows.keys()]
print(ratings_films)
print(sum(ratings_numbers) / len(ratings_numbers))
'''