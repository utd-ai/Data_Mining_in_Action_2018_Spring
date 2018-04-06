from regressor import DoctorRegressor
import time
from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler


# Создаём  экземпляр flask-a
app = Flask(__name__)
# Создаём эксземпляр нашей модели
doctor_regressor = DoctorRegressor()


# Парсинг формы
def parse_form(form):
    return {
        'experience': float(form.get('exp', 0.) or 0),
        'is_first_category': form.get('fst_cat') == 'true',
        'is_phd':  form.get('phd') == 'true',
        'proffesions': [ x.strip() for x in form.get('prof', '').split(',') ]
    }


# Основная функция, от flask-a нужен декоратор
@app.route("/price", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    # GET запрос - просто получение кода страницы - возвращем то, что есть
    if request.method == "GET":
        return render_template('hello.html')

    # POST запрос - получение кода страницы, но с учётом дополнительных посылаемых данных
    if request.method == "POST":
        # Извлекаем данные и парсим
        app.logger.info('POST request, start to parse data')
        obj = parse_form(request.form)
        app.logger.info('Data is parsed, the result is')
        app.logger.info(obj)
        # Делаем предсказание
        prediction = doctor_regressor.predict(obj)
        app.logger.info('The prediction is {}'.format(prediction))
        # Возвращаем страницу с правильно заполненными значениями
        return render_template(
            'hello.html', 
            is_phd='checked' if obj['is_phd'] else '',
            is_first_category='checked' if obj['is_first_category'] else '',
            proffesions=', '.join(obj['proffesions']),
            experience=str(obj['experience']),
            prediction=prediction
        )


if __name__ == "__main__":
    # Правильный способ логгировать данные - библиотека logging
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('demo.log', maxBytes=10000, backupCount=5)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(host='::', port=80, debug=True)
