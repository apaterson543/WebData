import tweepy as tw

# Fill out consumer information for Twitter API

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def get_auth():
    auth = tw.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,
                          access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api, tw
