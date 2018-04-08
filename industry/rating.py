import os

import pandas as pd


path = os.path.abspath('.')

files = [
    os.path.join(path, 'hw01', 'hw01_test_results.csv'),
    os.path.join(path, 'hw02', 'gb_impl_results.csv'),
    os.path.join(path, 'hw02', 'xgboost_params_results.csv'),
]

results = [pd.read_csv(file) for file in files]

total = {}
for result in results:
    result.columns = [x.strip() for x in result.columns]
    for _, row in result.iterrows():
        total[row.nickname] = total.get(row.nickname, 0) + row.Score

for num, result in enumerate(results):
    print('\n\nФайл', num + 1)
    for place, (_, row) in enumerate(result.sort_values(by='Score', ascending=False).iterrows()):
        print(place + 1, row.nickname, row.Score)

print('\n\nСуммарно по всем файлам')
sorted_total = sorted(total.items(), key=lambda x: x[1], reverse=True)
for place, (nick, score) in enumerate(sorted_total):
    print(place + 1, nick, score)
