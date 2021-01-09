import dataframe_image as dfi
import pandas as pd
import numpy as np

q1_user_0 = pd.read_csv('csv_files/q1_user_0.csv', index_col=0)
q1_user_1 = pd.read_csv('csv_files/q1_user_1.csv', index_col=0)
q1_user_2 = pd.read_csv('csv_files/q1_user_2.csv', index_col=0)
q2_top5 = pd.read_csv('csv_files/q2_top5.csv', index_col=0)
q2_bottom5 = pd.read_csv('csv_files/q2_bottom5.csv', index_col=0)
q3_sub_bottom_rec = pd.read_csv('csv_files/q3_sub_bottom_rec.csv', index_col=0)
q3_sub_top_rec = pd.read_csv('csv_files/q3_sub_top_rec.csv', index_col=0)
q4_top_rec = pd.read_csv('csv_files/q4_top_rec.csv', index_col=0)
q4_bad_rec = pd.read_csv('csv_files/q4_bad_rec.csv', index_col=0)
sub_me = pd.read_csv('csv_files/sub_me.csv', index_col=0)
top3use = pd.read_csv('csv_files/top3use.csv', index_col=0)

dfi.export(q1_user_0, 'tables/q1_user_0.png')
dfi.export(q1_user_1, 'tables/q1_user_1.png')
dfi.export(q1_user_2, 'tables/q1_user_2.png')
dfi.export(q2_top5, 'tables/q2_top5.png')
dfi.export(q2_bottom5,'tables/q2_bottom5.png')
dfi.export(q3_sub_bottom_rec, 'tables/q3_sub_bottom_rec.png')
dfi.export(q3_sub_top_rec, 'tables/q3_sub_top_rec.png')
dfi.export(q4_top_rec, 'tables/q4_top_rec.png')
dfi.export(q4_bad_rec, 'tables/q4_bad_rec.png')
dfi.export(sub_me, 'tables/sub_me.png')
dfi.export(top3use, 'tables/top3use.png')

# q1_user_0 = q1_user_0.replace(np.nan,'', regex=True)
# q1_user_1 = q1_user_1.replace(np.nan,'', regex=True)
# q1_user_2 = q1_user_2.replace(np.nan,'', regex=True)
# q3_not_seen_ratings = q3_not_seen_ratings.replace(np.nan,'', regex=True)
# q3_sub_bottom_rec = q3_sub_bottom_rec.replace(np.nan,'', regex=True)
# q3_sub_top_rec = q3_sub_top_rec.replace(np.nan,'', regex=True)
# q4_top_rec = q4_top_rec.replace(np.nan,'', regex=True)
# q4_bad_rec = q4_bad_rec.replace(np.nan,'', regex=True)
# q1_user_1 = q1_user_1.replace(np.nan,'', regex=True)

