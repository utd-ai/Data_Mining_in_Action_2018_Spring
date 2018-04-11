import os
from text_classification_params_checker import Checker
import json


if __name__ == '__main__':
    checker = Checker()
    scores = {}
    results = {}
    for filename in os.listdir('results/text_classification_params'):
        if filename.endswith('.json'):
            name = '_'.join(filename.split()[0].split('_')[-1:]).strip()
            score = checker.check('results/text_classification_params/' + filename)
            print(name, score)
            if score is not None:
                print('score is', max(round(2 ** (30 * (score - 0.875)), 2), 0.05))
                results[name] = score
            else:
                scores[name] = 0.05

    best_accuracy = max(results.values())
    for name in results:
        scores[name] = max(round(2 ** (30 * (results[name] - 0.875)), 2), 0.05)

    with open('text_classification_params_results.json', 'w') as f:
        json.dump(scores, f, indent=4)

    with open('text_classification_params_results.csv', 'w') as f:
        f.write('nickname, Score\n')
        for name in sorted(scores):
            f.write('{},{}\n'.format(name, scores[name]))
