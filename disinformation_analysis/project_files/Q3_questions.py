import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

tweets = pd.read_csv('200_tweets.csv')

num_tweets = len(tweets.index)
date_range = datetime.strptime(str(tweets['tweet time'].max()), '%Y%m%d%H%M%S') - datetime.strptime(str(tweets['tweet time'].min()), '%Y%m%d%H%M%S')

print(num_tweets)
print(date_range)
# 284
# 2 days, 5:09:19
all_accounts = []

for i, r in tweets.iterrows():
    account = r['account']
    exists = False
    for a in all_accounts:
        if a == account:
            exists = True
            break
    if exists == False:
        all_accounts.append(account)

print("Number of accounts = " + str(len(all_accounts)))

sns.set_style("whitegrid")
tweets_per_domain = pd.DataFrame(columns=['Domain','tweets'])#,'num accounts'
for index,row in tweets.iterrows():
    domain = row['domain']
    num_tweets = 0
    for i,r in tweets.iterrows():
        if domain == r['domain']:
            num_tweets += 1
    tweets_per_domain = tweets_per_domain.append({'Domain': domain, 'tweets':num_tweets}, ignore_index=True) #, 'num accounts':num_accounts

tweets_per_domain = tweets_per_domain.drop_duplicates()

accounts_per_domain = pd.DataFrame(columns=['domain','num accounts'])

for index,row in tweets_per_domain.iterrows():
    domain = row['domain']
    accounts = []
    num_accounts = 0
    for i,r in tweets.iterrows():
        exists = False
        if domain == r['domain']:
            for account in accounts:
                if account == r['account']:
                    exists = True
                    break
            if exists == False:
                accounts.append(r['account'])

    accounts_per_domain = accounts_per_domain.append({'domain':domain, 'num accounts': len(accounts)},ignore_index=True)

accounts_per_domain.to_csv("accounts_per_domain.csv", index=False)
tweets_per_domain.to_csv("tweets_per_domain.csv", index=False)

g = sns.catplot(x="domain", y="num tweets", kind="bar", data=tweets_per_domain)
g = (g.set_axis_labels('Domain',"Number of Tweets"))
plt.title('Tweets per Domain')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('tweets_per_domain')
# plt.show()
g = sns.catplot(x="domain", y="num accounts", kind="bar", data=accounts_per_domain)
g = (g.set_axis_labels('Domain',"Number of Accounts"))
plt.title('Accounts Tweeting Domains')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('accounts_per_domain')
