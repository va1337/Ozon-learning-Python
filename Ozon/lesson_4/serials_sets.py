anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

anya_set = set(anya.keys())
olya_set = set(olya.keys())
nastya_set = set(nastya.keys())
sveta_set = set(sveta.keys())
anya_nastya = list(anya_set & olya_set)
print('Общие фильмы у Ани и Оли: ' + ', '.join(list(anya_set & olya_set)))
print('Общие фильмы у Ани и Насти: ' + ', '.join(list(anya_set & nastya_set)))
print('Общие фильмы у Ани и Светы: ' + ', '.join(list(anya_set & sveta_set)))
