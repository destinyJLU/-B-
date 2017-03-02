# -*- coding: utf-8 -*-
from pylab import *
from sklearn.metrics import roc_curve,auc
from sklearn import cross_validation
from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
import numpy as np  
X = np.loadtxt(r"res.csv",delimiter=",",usecols=range(0,9445),skiprows=0)#获取特征
Y = np.loadtxt(r'phenotype.txt')	#结果信息
feature_train, feature_test, target_train, target_test = cross_validation.train_test_split(X, Y, random_state=42)
#clf = RandomForestClassifier(n_estimators = 100)
#alphaList = [0.1 ** i for i in range(-3,6)]
#aucList = []
#for alpha in alphaList:
#    clf = Ridge()
#    clf.fit(feature_train , target_train)
#    fpr, tpr, thresholds = roc_curve(target_test,clf.predict(feature_test))
#    roc_auc = auc(fpr, tpr)
#    aucList.append(roc_auc)
#print "AUC alpha"
#for i in range(len(aucList)):
#    print aucList[i],alphaList[i]
#print  clf.score(feature_test , target_test)
#f = open(r'e:\snp\name.txt')
#con = f.readlines()
#print "read file complete!"
#for line in con:
#	names = line.split(' ')
#rf = RandomForestRegressor(n_estimators=100) 
#for i in range(X.shape[1]):  
#	 score = cross_validation.cross_val_score(rf, X[:, i:i+1], y, scoring="r2",cv=cross_validation.ShuffleSplit(len(X), 2, .3))  
#	 scores.append((abs(round(np.mean(score), 3)), names[i]))
#print "Scores complete!"
#print sorted(scores, reverse=True)
#f.close()
#f = open(r'e:\snp\res.txt','w')
#n = sorted(scores,reverse=True)
#for (i,j) in n:
#		f.write('%f    %s\n'%(i,j))
#f.close()
