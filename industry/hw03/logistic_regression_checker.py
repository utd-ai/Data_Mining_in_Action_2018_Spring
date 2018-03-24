from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
import numpy as np
import os
import imp
import signal
import traceback
import sys


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def signal_handler(signum, frame):
    raise Exception("Timed out!")


class Checker(object):
    def __init__(self):
        self.X_data, self.y_data = make_classification(
            n_samples=10000, n_features=20, 
            n_classes=2, n_informative=20, 
            n_redundant=0,
            random_state=42
        )
        self.applications = 0

    def check(self, script_path):
        try:
            signal.signal(signal.SIGALRM, signal_handler)
            signal.alarm(20)
            algo_impl = imp.load_source('logistic_regression_{}'.format(self.applications), script_path)
            self.applications += 1
            algo = algo_impl.MyLogisticRegression(**algo_impl.LR_PARAMS_DICT)
            return np.mean(cross_val_score(algo, self.X_data, self.y_data, cv=2, scoring='accuracy'))
        except:
            traceback.print_exception(*sys.exc_info())
            return None


if __name__ == '__main__':
    print(Checker().check(SCRIPT_DIR + '/logistic_regression_example.py'))
