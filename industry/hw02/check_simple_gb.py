import os
from gb_impl_checker import Checker
import json


if __name__ == '__main__':
    checker = Checker()
    scores = {}
    results = {}
    for filename in os.listdir('dmia_gb_impl'):
        if filename.endswith('.py'):
            name = '_'.join(filename.split()[0].split('_')[-1:]).strip()
            score = checker.check('dmia_gb_impl/' + filename)
            print(name, score)
            if score is not None:
                results[name] = score
            else:
                scores[name] = 0.025


    best_neg_mse = max(results.values())
    for name in results:
        scores[name] = max(round(2 ** (10. * (results[name] - 0.779)), 3), 0.05)

    with open('gb_impl_results.json', 'w') as f:
        json.dump(scores, f, indent=4)

    with open('gb_impl_results.csv', 'w') as f:
        f.write('nickname, Score\n')
        for name in sorted(scores):
            f.write('{},{}\n'.format(name, scores[name]))
