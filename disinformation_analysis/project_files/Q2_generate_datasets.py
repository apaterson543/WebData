import pandas as pd
import csv

D1 = pd.read_csv("D1.csv")
D2 = pd.read_csv("D2_domains_and_tfreq.csv")
D3 = pd.read_csv("D3.csv")
comparisons = pd.DataFrame()
D1_D2 = []
D2_D3 = []
D1_D3 = []
D_All = []

#196443
#


for index_d1,row_d1 in D1.iterrows():
    for index_d2,row_d2 in D2.iterrows():
            if row_d1["Domain"] == row_d2["Domain"] and row_d1["Domain"] not in D1_D2:
                D1_D2.append(row_d1["Domain"])
for index_d1,row_d1 in D1.iterrows():
    for index_d3,row_d3 in D3.iterrows():
        if row_d1["Domain"] == str(row_d3["Domain"]).lower() and row_d1["Domain"] not in D1_D3:
            D1_D3.append((row_d1["Domain"]))
for index_d2, row_d2 in D2.iterrows():
    for index_d3, row_d3 in D3.iterrows():
        if row_d2["Domain"] == str(row_d3["Domain"]).lower() and row_d2["Domain"] not in D2_D3:
            D2_D3.append(row_d2["Domain"])
for domain in D1_D2:
    for index_d3, row_d3 in D3.iterrows():
        if domain == str(row_d3["Domain"]).lower() and domain not in D_All:
            D_All.append(domain)

size = max(len(D1_D2), len(D1_D3), len(D2_D3), len(D_All))

for i in range(size - len(D1_D2)):
    D1_D2.append("")
for i in range(size - len(D1_D3)):
    D1_D3.append("")
for i in range(size - len(D2_D3)):
    D2_D3.append("")
for i in range(size - len(D_All)):
    D_All.append("")

comparisons["D1_D2"] = D1_D2
comparisons["D1_D3"] = D1_D3
comparisons["D2_D3"] = D2_D3
comparisons["D_All"] = D_All

comparisons.to_csv("D_comparisons.csv")


