import clusters

def get_clusts(data):
    kclust5 = clusters.kcluster(data, k=5)
    kclust10 = clusters.kcluster(data, k=10)
    kclust20 = clusters.kcluster(data, k=20)
    return kclust5, kclust10, kclust20

def get_users_clust(kclust,users):
    user_clust = []
    for cluster in kclust:
        clust_add = []
        for i in range(len(cluster)):
            clust_add.append(users[cluster[i]])
        user_clust.append(clust_add)

    return user_clust

def output_clusters(kclust, k):

    for i in range(len(kclust)):
        file_name = "q4_data/k%s/cluster%s.txt" % (k,i)
        with open(file_name,'w') as file:
            file.writelines("%s\n" % user for user in kclust[i])

    return None

def main():
    file = ''
    with open('1000_terms.csv') as f:
        file = f.readlines()

    users, words, data = clusters.readfile(file)

    kclust5, kclust10, kclust20 = get_clusts(data)

    five = get_users_clust(kclust5,users)
    ten = get_users_clust(kclust10,users)
    twenty = get_users_clust(kclust20,users)

    print(five)
    print(ten)
    print(twenty)

    output_clusters(five,5)
    output_clusters(ten,10)
    output_clusters(twenty,20)

    return 0

if __name__ == '__main__':
    main()