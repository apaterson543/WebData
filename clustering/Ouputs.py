import pandas as pd

def print_dataframe(filename):
    df = pd.read_csv(filename, index_col='screen_name')
    print(df.astype(int))

print_dataframe("1000_terms.csv")