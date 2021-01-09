import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#
sns.set_style("whitegrid")
sns.set_palette(sns.color_palette(["#B32000","#0072E3"]))
friends = pd.read_csv('input_files/HW4-friend-count.csv')

num_users = friends.USER.count()
user_type = []
user_number = []
for i in range(num_users):
    user_type.append("friend")
    user_number.append("f"+str(i))


friends["USERTYPE"] = user_type
friends["USERNUMBER"] = user_number

stdev = friends.FRIENDCOUNT.std()
mean = friends.FRIENDCOUNT.mean()
median = friends.FRIENDCOUNT.median()
maximum = friends.FRIENDCOUNT.max()

friends = friends.append({"USER": "User", "FRIENDCOUNT": num_users, "USERTYPE": "user", "USERNUMBER": "U"}, ignore_index=True)
friends.sort_values(["FRIENDCOUNT"], axis=0, ascending=True, inplace=True)

textstr = '\n'.join((
    'mean = %.2f' % (mean,),
    'median = %.2f' % (median,),
    'sigma = %.2f' % (stdev,)))

print(textstr)
#
g = sns.catplot(x="USERNUMBER", y="FRIENDCOUNT", kind="point", data=friends, hue="USERTYPE")
g = (g.set_axis_labels('User', 'Number of Friends'))

plt.title('(source:friends)')

ticks = g.axes[0][0].get_yticks()
labels = ['{:,.00f}'.format(x) for x in ticks]
g.set_yticklabels(labels)
plt.xticks(rotation=90)
plt.text(5,4000, textstr)
plt.show()

