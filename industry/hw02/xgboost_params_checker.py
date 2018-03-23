#coding=utf-8

from sklearn.model_selection import cross_val_score
import xgboost as xgb
import pandas
import numpy as np
import signal
import os
import json
import sys


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def signal_handler(signum, frame):
    raise Exception("Timed out!")


class Checker(object):
    def __init__(self, data_path=SCRIPT_DIR + '/../seminar02/HR.csv'):
        df = pandas.read_csv(data_path)
        target = 'left'
        features = [c for c in df if c != target]
        self.target = np.array(df[target])
        self.data = np.array(df[features])

    def check(self, params_path):
        try:
            with open(params_path, 'r') as f:
                params = json.load(f)
                signal.signal(signal.SIGALRM, signal_handler)
                # Time limit на эту задачу 2 минуты
                signal.alarm(120)
                estimator = xgb.XGBClassifier(**params)
                score = np.mean(cross_val_score(
                    estimator, self.data, self.target,
                    scoring='accuracy', 
                    cv=3
                ))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            score = None
        
        return score


if __name__ == '__main__':
    print(Checker().check(SCRIPT_DIR + '/xgboost_params_example.json'))
