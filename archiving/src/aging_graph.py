import json
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
import csv

try:
    os.remove("../output/data_tables/age_of_archives.csv")
except:
    print("Clean slate")

sns.set_style("whitegrid");


number_of_files = len(os.listdir("../output/timemaps/"))
ages = []

for i in range(number_of_files):
    try:
        filepath = "../output/timemaps/timemap"+str(i)+".json"
        with open(filepath,"r") as file:
            data = json.load(file)
        # "datetime": "2020-07-17T20:46:07Z"
        pre_processed = data['mementos']['first']['datetime']
        pre = list(pre_processed)
        year = int(pre[0] + pre[1] + pre[2]+pre[3])
        month = int(pre[5] + pre[6])
        day = int(pre[8] + pre[9])
        hours = int(pre[11] + pre[12])
        minute = int(pre[14] + pre[15])
        sec = int(pre[17] + pre [18])

        first_mem = datetime(year,month,day,hours,minute,sec)
        collection_date = datetime.now()
        age = collection_date - first_mem
        ages.append(age.days)
        uris = data['mementos']['list']

        tup = [age.days, len(uris)]

        with open("../output/data_tables/age_of_archives.csv", "a+", newline='') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(tup)
    except:
        continue


age_data = pd.read_csv('../output/data_tables/age_of_archives.csv', header = None)


x = age_data[0]
y = age_data[1]
plt.xlabel("Age(days)")
plt.ylabel("Quantity of Mementos")
plt.title("(source: age_data)")
plt.scatter(x=x,y=y)


plt.show()
