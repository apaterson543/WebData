from recommendations import loadMovieLens
import pandas as pd
import Data

users = Data.get_users()
me = Data.get_me()
datas = Data.get_datas()
items = Data.get_items()

#me = {'user id': 0, 'age': 27, 'gender': 'M', 'occupation': 'student', 'zip code': 23508}
top_3_users = pd.DataFrame(columns=['user id', 'age', 'gender', 'occupation', 'zip code'])


for index,row in users.iterrows():
    if me['age'] == row ['age'] and me['gender'] == row['gender'] and me['occupation'] == row['occupation']:
        top_3_users = top_3_users.append(row, ignore_index=True)
    elif len(top_3_users) > 2:
        break


def find_users_top_and_bottom_3s(user):
    favorites = []
    least = []
    top_titles = []
    bottom_titles = []
    for index,row in datas.iterrows():
        if user['user id'] == row['user id'] and row['rating'] == 5 and len(favorites)<3:
            favorites.append(row['item id'])
        elif user['user id'] == row['user id'] and row['rating'] == 1 and len(least)<3:
            least.append(row['item id'])
        elif len(favorites) >= 3 and len(least) >= 3:
            break

    for i in range(len(favorites)):
        fav_movie = items.iloc[favorites[i] - 1]
        top_titles.append(fav_movie['movie title'])
        bad_movie = items.iloc[least[i] - 1]
        bottom_titles.append(bad_movie['movie title'])

    movies = pd.DataFrame({'favorites':top_titles, 'least Favorites':bottom_titles})

    return movies

def main():
    user0_movies = find_users_top_and_bottom_3s(top_3_users.iloc[0])
    user1_movies = find_users_top_and_bottom_3s(top_3_users.iloc[1])
    user2_movies = find_users_top_and_bottom_3s(top_3_users.iloc[2])
    print(user0_movies)
    print(user1_movies)
    print(user2_movies)
    top_3_users.to_csv('top3use.csv')
    print(top_3_users.iloc[2])
    user2_movies.to_csv('q1_user_2.csv')
    user1_movies.to_csv('q1_user_1.csv')
    user0_movies.to_csv('q1_user_0.csv')

if __name__ == '__main__':
    main()