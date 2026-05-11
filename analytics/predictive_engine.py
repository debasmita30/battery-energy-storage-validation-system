from sklearn.ensemble import IsolationForest
import numpy as np

class PredictiveEngine:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)

    def train(self, data):
        self.model.fit(np.array(data))

    def predict(self, row):
        return self.model.predict([row])[0]