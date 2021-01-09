import recommendations
import csv

prefs = recommendations.loadMovieLens()
person_list = list(prefs)
sub_me = person_list[429]

recommendations_list = recommendations.getRecommendations(prefs,sub_me)

top_5_rec = recommendations_list[0:5]
bottom_5_rec = recommendations_list[-5:]

with open('csv_files/q3_not_seen_ratings.csv', 'w') as output:
    csv_out = csv.writer(output)
    csv_out.writerow(['rating','movie title'])
    csv_out.writerows(recommendations_list)

with open('csv_files/q3_sub_top_rec.csv', 'w') as output:
    csv_out = csv.writer(output)
    csv_out.writerow(['rating','movie title'])
    csv_out.writerows(top_5_rec)

with open('csv_files/q3_sub_bottom_rec.csv', 'w') as output:
    csv_out = csv.writer(output)
    csv_out.writerow(['rating','movie title'])
    csv_out.writerows(bottom_5_rec)

