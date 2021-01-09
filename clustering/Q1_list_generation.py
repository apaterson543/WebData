import Tweepy
import pandas as pd

api,tw = Tweepy.get_auth()
users = tw.Cursor(api.search_users, q='filter:verified soccer',lang='en').items(250)

user_frame = pd.DataFrame(columns=['screen_name','followers_count','statuses_count'])

for user in users:
    if user.followers_count > 10000 and user.statuses_count > 5000:
        confirmed_user = { 'screen_name': user.screen_name,'followers_count':user.followers_count,
                           'statuses_count': user.statuses_count}
        user_frame = user_frame.append(confirmed_user, ignore_index=True)

user_frame = user_frame.drop_duplicates()

user_frame.to_csv('q1_data/100_users.csv', index=False)
