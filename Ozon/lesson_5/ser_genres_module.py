#Задание №2
def shows_from_genre(shows_dict, genre_name):
    return list(dict(filter(lambda elem: elem[1] == genre_name, shows_dict.items())).keys())


def ratings_mean_score(ratings_dict, shows_selected):
    ratings_new = {}
    for i in shows_selected:
        ratings_new = {i: ratings_dict[i] for i in shows_selected}
    shows_ratings = list(ratings_new.values())
    return sum(shows_ratings) / len(shows_ratings)
