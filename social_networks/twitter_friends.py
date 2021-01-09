import tweepy as tp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""



########################Gather data #####################################

# authorization of consumer key and consumer secret
auth = tp.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tp.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# the screen_name of the targeted user
screen_name = "weiglemc"
# initialize pandas dataframe
friends_frame = pd.DataFrame({"user":[],"followers_count":[], "is_follower":[]})
friend_count = 0
# gather all followers
followers = tp.Cursor(api.followers, screen_name=screen_name).items()
# append dataframe with followers and their respective follower counts
for follower in followers:
    frame_row = pd.DataFrame({"user": [follower.screen_name], "followers_count": [follower.followers_count],
                              "is_follower": ["follower"]})
    friends_frame = friends_frame.append(frame_row, ignore_index=True)
    friend_count += 1

# add initial user to dataframe
friends_frame = friends_frame.append({"user": "weiglemc", "followers_count": friend_count, "is_follower": "user"},
                                     ignore_index=True)

ordered_frame = friends_frame.sort_values(["followers_count"], ascending=True)

ordered_frame.to_csv("input_files/twitter.csv", index=False)


# #####################Graph data################################################

sns.set_style("whitegrid")
sns.set_palette(sns.color_palette(["#0072E3","#B32000"]))
friends = pd.read_csv('input_files/twitter.csv')

num_users = friends.USER.count()
user_number = []
for i in range(num_users):
        user_number.append(i)

#add user number to dataframe for graphing purposes
friends["USERNUM"] = user_number

stdev = friends.FOLLOWERS.std()
mean = friends.FOLLOWERS.mean()
median = friends.FOLLOWERS.median()
maximum = friends.FOLLOWERS.max()

textstr = '\n'.join((
    'mean = %.2f' % (mean,),
    'median = %.2f' % (median,),
    'sigma = %.2f' % (stdev,)))

g = sns.catplot(x="USERNUM", y="FOLLOWERS", kind="point", data=friends, hue="USERTYPE")
g = (g.set_axis_labels('User', 'Number of Friends'))

plt.title('(source:friends)')

ticks = g.axes[0][0].get_yticks()
labels = ['{:,.00f}'.format(x) for x in ticks]
g.set_yticklabels(labels)

# plot additions formatting
plt.axvline(288, 0, 0.17)
plt.text(10, 501000, textstr)
plt.locator_params(axis='x', nbins=25)

plt.show()
