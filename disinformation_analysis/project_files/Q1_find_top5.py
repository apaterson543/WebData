import pandas as pd

tweets_domain = pd.read_csv("D2_domains_and_tfreq.csv")
td = tweets_domain.drop_duplicates()
print(td.nlargest(5,'tweets'))
print(str(len(td)))

#Unique URLs 339

#                   URL  tweets
# 19  mintpressnews.com  1558.0
# 2              rt.com  1502.0
# 42       newsweek.com  1252.0
# 90       alternet.org  1221.0
# 29            cnn.com   756.0