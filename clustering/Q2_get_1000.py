import pandas as pd
import numpy as np


all_terms = pd.read_csv("q2_data/unordered_matrix.csv")
all_terms = all_terms.set_index('screen_name')

s = all_terms.sum()

all_terms = all_terms[s[s>1].nlargest(1000).index]

all_terms.to_csv('1000_terms.csv')













