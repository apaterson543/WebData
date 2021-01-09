import pandas as pd
import tweepy as tp
from datetime import datetime
import json

consumer_key = "GRzr421q8OcrcKTYPLJK98fgp"
consumer_secret = "TZl5FSVOnG5ev5lHZS2reuIZ92QeS09oTkptXDXnOAJF3VVa34"
access_token = "1309987286692638720-lk0t4cILn28K6WnfcXIFDtJlsUcC4b"
access_token_secret = "XpED0aQ7lzcD2OIPMr8K1Jm7KILtqqQzVQo7rVoMZM81Q"



########################Gather data #####################################

# authorization of consumer key and consumer secret
auth = tp.OAuthHandler(consumer_key, consumer_secret)


# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tp.API(auth, parser=tp.parsers.JSONParser(), wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

comparisons = pd.read_csv("D_comparisons.csv")
D3_shared = []

for index, row in comparisons.iterrows():
    D3_shared.append(row["D1_D3"])
    D3_shared.append(row["D2_D3"])

D3_shared = [x for x in D3_shared if isinstance(x, str)]

#
list_of_tweets = pd.DataFrame(columns=['tweet id', 'account', 'tweet time','domain','link'])
# , 'domain', 'link', 'tweet text'

for i in range(len(D3_shared)):
    tweets = api.search("url:" + D3_shared[i], lang="en", count=20)
    for status in tweets['statuses']:
        tweet_id = status['id_str']
        username = status['user']['screen_name']
        tweet_time = datetime.strptime(status['created_at'],'%a %b %d %H:%M:%S +0000 %Y').strftime("%Y%m%d%H%M%S")
        domain = D3_shared[i]
        try:
            link = str(status['entities']['urls'][0]['expanded_url'])
        except:
            link = "no extended link"
        tweet = {'tweet id':tweet_id, 'account':username, 'tweet time':tweet_time, 'domain':domain, 'link':link}
        list_of_tweets = list_of_tweets.append(tweet, ignore_index=True)

list_of_tweets.to_csv('200_tweets.csv', index=False)
print(list_of_tweets)



