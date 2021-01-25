import tweepy as tw
import os

# Fill out consumer information for Twitter API

consumer_key = os.environ.get("TP_CONSUMER_KEY")
consumer_secret = os.environ.get("TP_CONSUMER_SECRET")
access_token = os.environ.get("TP_ACCESS_TOKEN")
access_token_secret = os.environ.get("TP_ACCESS_TOKEN_SECRET")

def get_auth():
    auth = tw.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,
                          access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api, tw
