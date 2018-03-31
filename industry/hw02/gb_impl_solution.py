from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np


TREE_PARAMS_DICT = {'max_depth': 8, 'max_features': 3, 'random_state': 42}
TAU = 0.07


class SimpleGB(BaseEstimator):
    def __init__(self, tree_params_dict, iters, tau):
        self.tree_params_dict = tree_params_dict
        self.iters = iters
        self.tau = tau
        
    def fit(self, X_data, y_data):
        self.base_algo = LogisticRegression(C=0.0005).fit(X_data, y_data)
        self.estimators = []
        # p = 1 / (1 + exp(-a)) => a = - ln (1 / p - 1) = ln(p / (1 - p))
        curr_pred = - np.log(1. / self.base_algo.predict_proba(X_data)[:, 1] - 1)

        for iter_num in range(self.iters):
            # y это 0 или 1
            # a - сырое предсказание
            # f(a) = 1 / (1 + exp(-a)) - преобразование в вероятность
            # f'(a) = - exp(a) / (1 + exp(-a))^2 = - f(a) (1 - f(a))
            # log loss это (y log f(a) + (1 - y) log(1 - f(a)))

            # d/da (y log f(a) + (1 - y) log(1 - f(a))) = f'(a) (y/f(a) - (1 - y) / (1 - f(a)))
            fa = 1. / (1 + np.exp(-curr_pred))
            grad = - fa * (1. - fa) * (y_data / fa - (1. - y_data) / (1. - fa))
            algo = DecisionTreeRegressor(**self.tree_params_dict).fit(X_data, - grad)
            self.estimators.append(algo)
            curr_pred += self.tau * algo.predict(X_data)
        return self
    
    def predict(self, X_data):
        res = - np.log(1. / self.base_algo.predict_proba(X_data)[:, 1] - 1)
        for estimator in self.estimators:
            res += self.tau * estimator.predict(X_data)
        return res > 0.1 # этот порог можно варировать с целью повышения метрики
