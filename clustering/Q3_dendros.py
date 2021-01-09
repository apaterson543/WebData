import clusters

file = ''
with open('1000_terms.csv') as f:
    file = f.readlines()

screen_names, words, data = clusters.readfile(file)


print(clusters.readfile(file))
clust = clusters.hcluster(data)
#
#clusters.printclust(clust, labels=screen_names)
clusters.drawdendrogram(clust,screen_names,jpeg='q3_data/userclust.jpg')
