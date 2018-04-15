import xgboost as xgb
import json


class DoctorRegressor(object):

    def __init__(self, resources_dir='resources/'):
        # Загружаем модель
        self.model = xgb.XGBRegressor()
        booster = xgb.Booster()
        booster.load_model('{}/xgboost_model'.format(resources_dir))
        self.model._Booster = booster
        # Загружаем список специализаций
        with open('{}/prof_set_list.json'.format(resources_dir), 'r') as f:
            self.prof_set_list = json.load(f)


    def extract_features(self, doctor):
        features = []
        # 0 - experience
        features.append(doctor['experience'] or 0)
        # 1 - is_first_category
        features.append(float(doctor['is_first_category']))
        # 2 - is_phd
        features.append(float(doctor['is_phd']))
        # 3 - len(proffesions)
        features.append(len(doctor['proffesions']))
        # 4 - 87 one hot proffesions
        for p in self.prof_set_list:
            features.append(float(p in doctor['proffesions']))
        return features


    def predict(self, obj):
        # Применение модели
        return self.model.predict([self.extract_features(obj)])[0]
