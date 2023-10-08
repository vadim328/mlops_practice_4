import pandas as pd
import os
import pickle
import json
from catboost import CatBoostClassifier
from sklearn import metrics


cbc = pickle.load(open('models/model.pkl', 'rb')) 

test_df = pd.read_csv('data/prepared/test.csv', sep=',')

X = test_df.drop("outcome", axis = 1)
y = test_df['outcome']

y_pred = cbc.predict(X)

score = metrics.accuracy_score(y, y_pred)

evaluate = {'score': score}

with open('evaluate/score.json', 'w') as f:
    json.dump(evaluate, f)

