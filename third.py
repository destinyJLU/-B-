# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:01:56 2016
@author: Administrator
"""
from pylab import *
from sklearn import cross_validation
from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestClassifier 
from sklearn import svm
import numpy as np  
LEN = []
for i in range(0,300):
    f = open(r"e:\snp\gene_info\gene_%s.dat"%str(i+1))
    con = f.readlines()
    LEN.append(len(con))
    f.close()
pos = 0
SCORE = []
for i in range(0,300):
    X = np.loadtxt(r"e:\snp\res.csv",delimiter=",",usecols=range(pos,pos+LEN[i]),skiprows=0)
    pos = pos+LEN[i]
    #Y = np.loadtxt(r'e:\snp\multi_phenos.txt',delimiter=" ",usecols=range(0,10),skiprows=0)
    Y = np.loadtxt(r'e:\snp\phenotype.txt')
    feature_train, feature_test, target_train, target_test = cross_validation.train_test_split(X, Y, test_size=0.10, random_state=42)
    clf = RandomForestClassifier(n_estimators = 100)
    s = clf.fit(feature_train , target_train)
    #clf = svm.SVC(kernel='linear',C=1).fit(feature_train,target_train)
    print  clf.score(feature_test , target_test)