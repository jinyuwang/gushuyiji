#!/usr/bin/python

import pandas as pd
import statsmodels.api as sm

POINT = 0.5

train = pd.read_csv("output/lr_train.csv")
train_cols = train.columns[1:]
logit = sm.Logit(train['target'], train[train_cols])
result = logit.fit()
result.summary()

combos = pd.read_csv("lr_vectors.csv")
train_cols = combos.columns[2:]
combos['prediction'] = result.predict(combos[train_cols])

predicts = defaultdict(set)
for term in combos.values:
    uid, bid, prediction = str(int(term[0])), str(int(term[1])), term[4]
if prediction > POINT:
    predicts[uid].add(bid)
