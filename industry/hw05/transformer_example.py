# coding=utf-8
import numpy as np
from sklearn.base import TransformerMixin
from collections import Counter


LR_PARAMS_DICT = {}


class CustomTransformer(TransformerMixin):
    
    def fit(self, X, y):
        self.cnt = Counter()
        for i in range(X.shape[1]):
            for j in range(np.max(X[:, i])):
                indices = X[:, i] == j
                if np.sum(indices) > 0:
                    val = y[indices].mean()
                else:
                    val = y.mean()
                self.cnt[(i, j)] = val
                
        return self
    
    def transform(self, X):
        X_new = np.copy(X)
        for i in range(X.shape[1]): 
            for j in range(np.max(X[:, i])):
                indices = X[:, i] == j
                if np.sum(indices) > 0:
                    X_new[indices, i] = self.cnt[(i, j)]
        return X_new
