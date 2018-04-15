import pandas
import numpy as np


df = pandas.read_csv('dmia_raw.csv')
df = df.loc[:, ['nickname', 'Score']]
df['Score'] = df['Score'].apply(lambda x: max(0.1, np.exp(0.5 * (float(x.split('/')[0]) - 13.))))

df.to_csv('hw01_test_results.csv')