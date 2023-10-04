import pandas as pd


url_train = 'https://drive.google.com/uc?id=1S9Z38cffP2KSaXB-vW0BKpzSuWFhhKZM'
url_test = 'https://drive.google.com/uc?id=1n8t901VZYPhF6wSVz9-tlSm2y-Kagax9'
train_df = pd.read_csv(url_train)
test_df = pd.read_csv(url_test)
train_df.to_csv('/home/data_srv/git/mlops_practice_2/data/raw/train.csv', sep=',', index = False)
test_df.to_csv('/home/data_srv/git/mlops_practice_2/data/raw/test.csv', sep=',', index = False)

