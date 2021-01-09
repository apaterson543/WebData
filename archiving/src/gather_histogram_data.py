import json
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import csv

sns.set_style("whitegrid")

number_of_files = len(os.listdir("../output/timemaps/"))
mementos_in_files = []
for i in range(number_of_files):
    try:
        filepath = "../output/timemaps/timemap"+str(i)+".json"
        with open(filepath,"r") as file:
            data = json.load(file)

        uris = data['mementos']['list']
    except:
        print('finished')
        break

    mementos_in_files.append(len(uris))


with open("../output/data_tables/number_of_mementos.csv", "w", newline='') as csvfile:

    write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for mem in mementos_in_files:
        write.writerow([mem])

mementos = pd.read_csv('../output/data_tables/number_of_mementos.csv', header = None)

ax = sns.distplot(mementos[mementos[0]<40000][0], kde=False)

ax.set_xlabel ('Number of Mementos')
ax.set_ylabel ('Frequency of Occurence')
ax.set_title('(source: mementos_in_files)')

ticks = ax.get_xticks()
plt.show()


