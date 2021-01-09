import Tweepy
import pandas as pd

api, tw = Tweepy.get_auth()

users = pd.read_csv('q1_data/100_users.csv')

for index, row in users.iterrows():
    statuses = tw.Cursor(api.user_timeline, screen_name=row['screen_name'], lang='en', include_rts=False).items(200)
    filename = "q1_data/tweets_by_user/user" + str(index) + ".txt"
    with open(filename, 'a') as file:
        file.write(row['screen_name'] + ' \n')
        for status in statuses:
            file.write(status.text)
    print(index)
