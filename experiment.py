# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:29:04 2017

@author: destiny
"""
import operator
import xgboost as xgb
import pandas as pd
def ceate_feature_map(features):  
    outfile = open('xgb.fmap', 'w')  
    i = 0  
    for feat in features:  
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))  
        i = i + 1  
    outfile.close()

if __name__ == "__main__":
    X = pd.read_csv("res.csv",usecols=range(0,9445))
    y = pd.read_csv("phenotype.csv")
    params = {  
            'min_child_weight': 100,  
            'eta': 0.02,  
            'colsample_bytree': 0.7,  
            'max_depth': 12,  
            'subsample': 0.7,  
            'alpha': 1,  
            'gamma': 1,  
            'silent': 1,  
            'verbose_eval': True,  
            'seed': 12  
        }
    rounds = 10
    xgtrain = xgb.DMatrix(X, label=y)
    bst = xgb.train(params, xgtrain, num_boost_round=rounds)
    features = [x for x in X.columns]  
    ceate_feature_map(features)  
  
    importance = bst.get_fscore(fmap='xgb.fmap')  
    importance = sorted(importance.items(), key=operator.itemgetter(1))  
  
    df = pd.DataFrame(importance, columns=['feature', 'fscore'])  
    df['fscore'] = df['fscore'] / df['fscore'].sum()  
    df.to_csv("feat_importance.csv", index=False) 