import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dataframe_image as dfi


top_Q3 = pd.read_csv("tweets_per_domain.csv")
top_Q3 = top_Q3.sort_values(["tweets"], ascending=False)
D1 = pd.read_csv("D1.csv")
D2 = pd.read_csv("D2_domains_and_tfreq.csv")

top_Q3 = top_Q3.sort_values(['tweets'], ignore_index=True, ascending=False)

top_D1 = pd.DataFrame(columns=["Domain","tweets"])
for index, row in top_Q3.iterrows():
    domain = row['Domain']
    for i, r in D1.iterrows():
        if r['Domain'] == domain:
            top_D1 = top_D1.append({'Domain':domain,'tweets':r['# Citations in our Alternative Narrative Tweets']}, ignore_index=True)
top_D1 = top_D1.sort_values(['tweets'], ascending=False)

top_D2 = pd.DataFrame(columns=["Domain","tweets"])
for index, row in top_Q3.iterrows():
    domain = row['Domain']
    for i, r in D2.iterrows():
        if r['Domain'] == domain:
            top_D2 = top_D2.append({'Domain':domain,'tweets':r['tweets']}, ignore_index=True)

top_D2 = top_D2.drop_duplicates()
top_D2 = top_D2.sort_values(['tweets'],ascending=False)

top_5_Q3 = top_Q3.head(5)
top_5_D1 = top_D1.head(5)
top_5_D2 = top_D2.head(5)

all_data = pd.DataFrame(columns=["Domain","tweets D1", "tweets D2", "tweets Q3"])

for index,row in top_5_Q3.iterrows():
    all_data = all_data.append({'Domain':row['Domain'], 'tweets D1':0, 'tweets D2':0, 'tweets Q3':row['tweets']}, ignore_index=True)

for index,row in top_5_D1.iterrows():
    exists = False
    domain = row['Domain']
    for i,r in all_data.iterrows():
        if r['Domain'] == domain:
            all_data.at[i,'tweets D1'] = row['tweets']
            exists = True
            break
    if exists == False:
        all_data = all_data.append({'Domain':domain, 'tweets D1':row['tweets'], 'tweets D2':0, 'tweets Q3':0}, ignore_index=True)

for index,row in top_5_D2.iterrows():
    exist = False
    domain = row['Domain']
    for i,r in all_data.iterrows():
        if r['Domain'] == domain:
            print(domain)
            all_data.at[i,'tweets D2'] = row['tweets']
            exist = True
            break
    if exist == False:
        print(domain)
        all_data = all_data.append({'Domain':domain, 'tweets D1':0, 'tweets D2':row['tweets'], 'tweets Q3':0}, ignore_index=True)

# print(top_5_Q3)
# print(top_5_D1)
# print(top_5_D2)
dfi.export(top_5_D1,'top_5_D1.png')
dfi.export(top_5_D2,'top_5_D2.png')
dfi.export(top_5_Q3,'top_5_Q3.png')

print(all_data)

'''
Plotting method gathered from: https://python-graph-gallery.com/11-grouped-barplot/
'''


# set width of bar
barWidth = 0.25

# set height of bar
bars1 = [x for x in all_data['tweets D1']]
bars2 = [x for x in all_data['tweets D2']]
bars3 = [x for x in all_data['tweets Q3']]
domains = [d for d in all_data['Domain']]
print(bars1)
print(bars2)
print(bars3)
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='D1')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='D2')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='Q3')

# Add xticks on the middle of the group bars
plt.xlabel('Domains', fontweight='bold')
plt.ylabel('Number of Tweets',fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], domains)

# Create legend & Show graphic
plt.legend()
plt.title('Tweet Frequency Per Data Set On Top Domains')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('Q4_comparison_graph')
plt.show()