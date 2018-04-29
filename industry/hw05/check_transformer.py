import os
import json
import re
from transformer_checker import Checker


if __name__ == '__main__':
    checker = Checker()
    scores = {}
    results = {}
    for filename in os.listdir('transformers'):
        if filename.endswith('.py'):
            name = ''.join(re.split('transformer_| - ', filename)[:-1]).strip()
            score = checker.check('transformers/' + filename)
            print(name, score)
            if score is not None:
                print('score is', max(round(2 ** (10 * (score - 0.945)), 2), 0.05))
                results[name] = score
            else:
                scores[name] = 0.05

    best_accuracy = max(results.values())
    for name in results:
        scores[name] = max(round(2 ** (10 * (results[name] - 0.945)), 2), 0.05)

    with open('transformer_results.json', 'w') as f:
        json.dump(scores, f, indent=4)

    with open('transformer_results.csv', 'w') as f:
        f.write('nickname, Score\n')
        for name in sorted(scores):
            f.write('{},{}\n'.format(name, scores[name]))
