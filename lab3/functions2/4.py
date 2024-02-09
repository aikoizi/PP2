def list_movies(listok):
    sum=0
    for i in listok:
        sum+=i['IMDB']

    return sum/len(listok)