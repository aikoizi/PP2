
def cate_imdb(movies_list, category):
    cate_movies = [movie["imdb"] for movie in movies_list if movie["category"] == category]
    if not cate_movies:
        return 0
    return sum(cate_movies) / len(cate_movies)


