import dataframe_image as dfi
import pandas as pd


k5 = pd.read_csv('q4_data/k5.csv').fillna('')
k10 = pd.read_csv('q4_data/k10.csv').fillna('')
k20 = pd.read_csv('q4_data/k20.csv').fillna('')

dfi.export(k5, 'q4_data/k_tables/k5_table.png')
dfi.export(k10, 'q4_data/k_tables/k10_table.png')
dfi.export(k20, 'q4_data/k_tables/k20_table.png')