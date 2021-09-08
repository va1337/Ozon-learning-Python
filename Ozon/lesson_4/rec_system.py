import random
shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
vasya_shows = dict(filter(lambda elem: elem[1] != 'фэнтази', shows.items()))
vasya_ratings = dict(filter(lambda elem: elem[1] >= 0.85, ratings.items()))
films_for_watch = list(set(vasya_shows) & set(vasya_ratings))
while True:
    film = random.choice(list(shows.items()))[0]
    print(f'Васе был предложен следующий фильм - {film}')
    if film in films_for_watch:
        print('Сериал подходит Васе')
    else:
        print('Сериал не подходит Васе (жанр фэнтази или рейтинг <0.85)')
    print("Вася, хочешь ли ты смотреть этот сериал? Напиши 'да' или 'нет' " )
    answer = str(input())
    while answer not in ('да', 'нет'):
        print("Напишите 'да' или 'нет' ")
        answer = str(input())
    if answer == 'нет':
        continue
    if answer == 'да':
        print(f'Вася выбрал следующий фильм - {film}')
        break