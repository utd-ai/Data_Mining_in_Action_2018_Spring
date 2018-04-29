import pandas
import json
import numpy as np


df = pandas.read_csv('results_raw.csv')
df = df[['Email address', 'Score']]
df['Score'] = df['Score'].apply(lambda x: max(0.1, float(x.split('/')[0]) / 8.))

df.to_csv('results.csv', header=None, index=False)
with open('results.json', 'w') as f:
    json.dump({
        obj['Email address']: obj['Score']
        for _, obj in df.iterrows()    
    }, f, indent=4)

