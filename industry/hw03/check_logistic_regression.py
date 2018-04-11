import os
from logistic_regression_checker import Checker
import json


if __name__ == '__main__':
    checker = Checker()
    scores = {}
    results = {}
    for filename in os.listdir('results/logistic_regression'):
        if filename.endswith('.py'):
            name = '_'.join(filename.split()[0].split('_')[-1:]).strip()
            score = checker.check('results/logistic_regression/' + filename)
            print(name, score)
            if score is not None:
                print('score is', max(round(2 ** (30 * (score - 0.785)), 2), 0.05))
                results[name] = score
            else:
                scores[name] = 0.05

    best_accuracy = max(results.values())
    for name in results:
        scores[name] = max(round(2 ** (30 * (results[name] - 0.785)), 2), 0.05)

    with open('logistic_regression_results.json', 'w') as f:
        json.dump(scores, f, indent=4)

    with open('logistic_regression_results.csv', 'w') as f:
        f.write('nickname, Score\n')
        for name in sorted(scores):
            f.write('{},{}\n'.format(name, scores[name]))
