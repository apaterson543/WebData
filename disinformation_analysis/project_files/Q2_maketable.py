import dataframe_image as dfi
import pandas as pd
import numpy as np

df_table = pd.read_csv('D_comparisons.csv', index_col=0)
df_table = df_table.replace(np.nan,'', regex=True)
dfi.export(df_table, 'Q2_comparisons_table.png')