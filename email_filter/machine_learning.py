from joblib import load
import numpy as np


class SpamModel:
    def __init__(self):
        self.__model = load('email_filter/static/machine_learning/spammodel.joblib')
        self.__vectorizer = load('email_filter/static/machine_learning/vectorizer.joblib')

    def predict(self, text):
        vectorized_text = self.__vectorizer.transform([text])
        values = self.__model.predict_proba(vectorized_text) * 100
        rounded_values = np.around(values[0], decimals=2)
        return rounded_values
