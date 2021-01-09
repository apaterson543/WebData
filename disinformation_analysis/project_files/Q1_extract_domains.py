import pandas as pd
import re
import csv


d1_extended = pd.read_csv("D2_extended.csv")
d1_extended = d1_extended.drop(d1_extended.columns[0], axis=1)
num_redirects = 0
num_200 = 0
num_404 = 0
num_4__ = 0
unique_domains = []
tweets_per_domain = []
for index,row in d1_extended.iterrows():
    if row["Redirect"] == True:
        num_redirects += 1
    if row["Status Code"] == "200":
        num_200 += 1
    if row["Status Code"] == "404":
        num_404 += 1
    elif "200" not in row["Status Code"]:
        num_4__ += 1

    #Find unique Domains
    domain = str(re.findall('://www.([\w\-\.]+)',row["Final URL"]))[2:-2]

    unique = True
    for dom in unique_domains:

        if domain == str(dom)[2:-2]:
            unique = False
            break
    if unique == True:
        unique_domains.append(str(domain))

print("Num Unique URLs: " + str(len(unique_domains)))
# Number of tweets per domain
for d in unique_domains:
    tweet_count = 0.0
    domain = str(d)


    for index,row in d1_extended.iterrows():
        single_url_domain = str(re.findall('://www.([\w\-\.]+)',row["Final URL"]))[2:-2]
        if domain == single_url_domain:
            tweet_count += float(row["total_freq"])

    tweets_per_domain.append([domain,tweet_count])
    print(tweet_count)

with open("D2_domains_and_tfreq.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(tweets_per_domain)


#tweets_per_domain.sort(key=lambda x: x[[1]], reverse=True )
print("Redirects: " + str(num_redirects))  # 792
print("200: " + str(num_200))  # 1166
print("404: " + str(num_404))  # 206
print("4**: " + str(num_4__))  # 307
# print("Num Unique URLs: " + str(len(unique_domains)))
# print(tweets_per_domain)