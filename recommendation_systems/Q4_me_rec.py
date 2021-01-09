import recommendations
import csv

prefs = recommendations.loadMovieLens()

similarities = recommendations.calculateSimilarItems(prefs)

good_movie = similarities['Reservoir Dogs (1992)']
not_for_me = similarities['Winnie the Pooh and the Blustery Day (1968)']

with open('csv_files/q4_top_rec.csv', 'w') as output:
    csv_out = csv.writer(output)
    csv_out.writerow(['correlation','movie title'])
    csv_out.writerows(good_movie[0:5])

with open('csv_files/q4_bad_rec.csv', 'w') as output:
    csv_out = csv.writer(output)
    csv_out.writerow(['correlation','movie title'])
    csv_out.writerows(not_for_me[0:5])
