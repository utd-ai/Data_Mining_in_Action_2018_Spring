import os
from svm_checker import Checker
import json


if __name__ == '__main__':
    checker = Checker()
    scores = {}
    results = {}
    for filename in os.listdir('python_impl_svm'):
        if filename.endswith('.py'):
            name = '_'.join(filename.split()[0].split('_')[1:]).strip()
            score = checker.check('python_impl_svm/' + filename)
            print name, score
            if score is not None:
                results[name] = score
            else:
                scores[name] = 0.025

    best_neg_mse = max(results.values())
    for name in results:
        scores[name] = max(round(2 ** (15 * (results[name] - best_neg_mse)), 3), 0.05)

    with open('python_impl_svm_results.json', 'w') as f:
        json.dump(scores, f, indent=4)

    with open('python_impl_svm_results.csv', 'w') as f:
        for name in sorted(scores):
            f.write('{},{}\n'.format(name, scores[name]))
