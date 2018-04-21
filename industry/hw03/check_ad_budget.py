import os
from ad_budget_checker import Checker
import json


if __name__ == '__main__':
    checker = Checker()
    scores = {}
    results = {}
    for filename in os.listdir('results/ad_budget'):
        if filename.endswith('.py'):
            name = '_'.join(filename.split()[0].split('_')[-1:]).strip()
            score = checker.check('results/ad_budget/' + filename)
            print(name, score)
            if score is not None:
                print('score is', max(round(score / 7.5, 2), 0.05))
                results[name] = score
            else:
                scores[name] = 0.05

    best_accuracy = max(results.values())
    for name in results:
        scores[name] = max(round(results[name] / 7.5, 2), 0.05)

    with open('ad_budget_results.json', 'w') as f:
        json.dump(scores, f, indent=4)

    with open('ad_budget_results.csv', 'w') as f:
        f.write('nickname, Score\n')
        for name in sorted(scores):
            f.write('{},{}\n'.format(name, scores[name]))
