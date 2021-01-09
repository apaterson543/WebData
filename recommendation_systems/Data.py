import pandas as pd

def get_users():
    users = pd.read_csv('ml-100k/u.user', header=None, sep='|')
    users = users.rename({0: 'user id', 1: 'age', 2: 'gender', 3: 'occupation', 4: 'zip code'}, axis='columns')
    return users

def get_me():
    me = {'user id': 0, 'age': 27, 'gender': 'M', 'occupation': 'student', 'zip code': 23508}
    return me

def get_datas():
    datas = pd.read_csv('ml-100k/u.data', header=None, sep='\s+')
    datas = datas.rename({0: 'user id', 1: 'item id', 2: 'rating', 3: 'timestamp'}, axis='columns')
    return datas

def get_items():
    items = pd.read_csv('ml-100k/u.item', header=None, sep='|', encoding='iso-8859-1')
    items = items.rename({0: 'movie id', 1: 'movie title', 2: 'release date', 3: 'video release date', 4: 'IMDb URL',
                          5: 'unknown', 6: 'Action', 7: 'Adventure', 8: 'Animation', 9: "Children's", 10: "Comedy",
                          11: "Crime",
                          12: "Documentary", 13: "Drama", 14: "Fantasy", 15: "Film-Noir", 16: "Horror", 17: "Musical",
                          18: "Mystery", 19: "Romance", 20: "Sci-Fi", 21: "Thriller", 22: "War", 23: "Western"},
                         axis='columns')
    return items