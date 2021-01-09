import pandas as pd
import Data
import recommendations

users = Data.get_users()
prefs = recommendations.loadMovieLens()

person_list = list(prefs)

sub_me = person_list[429]

top5 = recommendations.topMatches(prefs,sub_me)
bottom5 = recommendations.leastMatches(prefs,sub_me)
print(top5)
print(bottom5)
top5_frame = pd.DataFrame()
bottom5_frame = pd.DataFrame()

for i in range(len(top5)):
    top5_frame = top5_frame.append(users.iloc[int(top5[i][1])-1])
    bottom5_frame = bottom5_frame.append(users.iloc[int(bottom5[i][1])-1])

top_correlations = []
bottom_correlations = []

for i in range(len(top5)):
    top_correlations.append(str(top5[i][0]))
    bottom_correlations.append(str(bottom5[i][0]))

top5_frame['correlation'] = top_correlations
bottom5_frame['correlation'] = bottom_correlations

top5_frame.to_csv('csv_files/q2_top5.csv')
bottom5_frame.to_csv('csv_files/q2_bottom5.csv')

print(top5_frame)
print(bottom5_frame)