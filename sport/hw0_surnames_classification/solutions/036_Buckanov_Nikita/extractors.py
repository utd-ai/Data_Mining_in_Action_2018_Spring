from sklearn.base import BaseEstimator, TransformerMixin
from scipy import sparse
import re
import pymorphy2


class Upper(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([int(t[0].isupper()) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([int(t[0].isupper()) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing

class All_upper(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([int(t.isupper()) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([int(t.isupper()) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing
    
class All_lower(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([int(t.islower()) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([int(t.islower()) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing

class Word_length(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([len(t) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([len(t) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing

class Vow_count(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([len(re.findall('[уеыаоэяию]', t, re.IGNORECASE)) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([len(t) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing

class Con_count(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([len(t) - len(re.findall('[уеыаоэяию]', t, re.IGNORECASE)) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([len(t) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing
    
class Spec_count(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([len(t) - len(re.findall('[- ]', t, re.IGNORECASE)) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([len(t) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing
    
class Tolower(BaseEstimator, TransformerMixin):
    def fit_transform(self, X, y=None):
        return [t.lower()[:-5] for t in X]
    def transform(self, X, y=None):
        return [t.lower()[:-5] for t in X]
    def fit(self, X, y=None):
        return  # generally does nothing
       
class Pymorphy_predict(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
    def fit_transform(self, X, y=None):
        return sparse.csr_matrix([sum([p.score*int('фам' in p.tag.cyr_repr) for p in self.morph.parse(t)]) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([sum([p.score*int('фам' in p.tag.cyr_repr) for p in self.morph.parse(t)]) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing
    def predict_proba(self,X):
        return[ [1-sum([p.score*int('фам' in p.tag.cyr_repr) for p in self.morph.parse(t)]), 
                   sum([p.score*int('фам' in p.tag.cyr_repr) for p in self.morph.parse(t)])] for t in X ] 

class Pymorphy_normal(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
    def fit_transform(self, X, y=None): 
        return sparse.csr_matrix([ int(t in [p.normal_form for p in self.morph.parse(t)]) for t in X]).transpose()
    def transform(self, X, y=None):
        return sparse.csr_matrix([ int(t in [p.normal_form for p in self.morph.parse(t)]) for t in X]).transpose()
    def fit(self, X, y=None):
        return  # generally does nothing
