import re
import os
import tweepy as tw
import pandas as pd
import threading
import requests

## gather 1000 unique links from tweets in twitter
## resolve any shortened links and return full link instead
## no links from twitter domain

auth = tw.OAuthHandler('', '')
auth.set_access_token('',
                      '')
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search_word = '#coronavirus'
date_since = '2020-3-14'
twitter_link = 'twitter.com'

unique_urls = []
tweets = tw.Cursor(api.search, q=search_word, lang='en', since=date_since).items(1000000)


def collect_links():
    count = 0
    three_hundred_codes = 0
    shortened = 0

    for tweet in tweets:
        if len(unique_urls) < 1000:

            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            urls = re.findall(regex, tweet.text)
            """
            regular expression for finding a url found at:
            https://www.geeksforgeeks.org/python-check-url-string/#:~:text=To%20find%20the%20URLs%20in,returned%20in%20the%20order%20found.
            """

            count += 1
            if count % 100 == 0:
                print(str(count)+" Tweets Read")

            for url in urls:
                try:
                    response = requests.get(url[0])
                    if response.status_code == 200 and str(response.url).find(twitter_link) == -1:
                        full = response.url

                        if url[0] != full:
                            shortened += 1

                        uni = True
                        for link in unique_urls:
                            if full == link:
                                uni = False
                                break
                        if uni:
                            unique_urls.append(full)
                    elif response.status_code == 300:
                        three_hundred_codes += 1
                    print(count/1000)
                except:
                    print(count/1000)
        else:
            break

    for uri in unique_urls:
        print(uri)
    outfile = open('../output/unique_urls.txt', 'a')

    for uri in unique_urls:
        outfile.write(str(uri) + '\n')

    outfile.close()

    print(len(unique_urls))
    print(three_hundred_codes)
    return exit(0)


if __name__ == "__main__":
    collect_links()

