# coding=utf-8

from sklearn.model_selection import cross_val_score
import numpy as np
import os
import sys
import imp
import signal
import pandas


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
        self.application = 0

    def check(self, script_path):
        try:
            signal.signal(signal.SIGALRM, signal_handler)
            # Time limit на эту задачу 1 минута
            signal.alarm(60)
            gb_impl = imp.load_source('gb_impl_{}'.format(self.application), script_path)
            self.application += 1
            # Обучаться будет на 100 итерациях, чтобы одинаковый масштаб был
            algo = gb_impl.SimpleGB(
                tree_params_dict=gb_impl.TREE_PARAMS_DICT,
                iters=100,
                tau=gb_impl.TAU
            )
            return np.mean(cross_val_score(algo, self.data, self.target, cv=3, scoring='accuracy'))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return None


if __name__ == '__main__':
    print(Checker().check(SCRIPT_DIR + '/gb_impl_example.py'))
