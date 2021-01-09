import clusters


with open('1000_terms.csv') as f:
    file = f.readlines()

users, words, data = clusters.readfile(file)

coords = clusters.scaledown(data)
clusters.draw2d(coords,users,jpeg='q5_data/twitter_user_MDS.jpg')