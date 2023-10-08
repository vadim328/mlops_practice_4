import pandas as pd
import numpy as np
import yaml
import os
import pickle
from catboost import CatBoostClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split


params = yaml.safe_load(open("params.yaml"))

train_df = pd.read_csv('data/prepared/train.csv', sep=',')

X = train_df.drop("outcome", axis = 1)
y = train_df['outcome']

n_estimators = params["estimator"]["n_estimators"]
#split_ratio = params["split"]["split_ratio"]

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratio, random_state=42)

cbc = CatBoostClassifier(verbose=0, n_estimators=n_estimators)
cbc.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(cbc, f)
