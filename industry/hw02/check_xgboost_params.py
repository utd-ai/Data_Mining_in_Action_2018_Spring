import os
from xgboost_params_checker import Checker
import json


if __name__ == '__main__':
    checker = Checker()
    scores = {}
    results = {}
    for filename in os.listdir('xgboost_params'):
        if filename.endswith('.json'):
            name = '_'.join(filename.split()[0].split('_')[-1:]).strip()
            score = checker.check('xgboost_params/' + filename)
            print name, score
            if score is not None:
                results[name] = score
            else:
                scores[name] = 0.025

    best_accuracy = max(results.values())
    for name in results:
        scores[name] = max(round(2 ** (30 * (results[name] - best_accuracy)), 2), 0.05)

    with open('xgboost_params_results.json', 'w') as f:
        json.dump(scores, f, indent=4)

    with open('xgboost_params_results.csv', 'w') as f:
        for name in sorted(scores):
            f.write('{},{}\n'.format(name, scores[name]))
