# -*- coding: utf-8 -*-

"""
Copyright (c) 2016 Randal S. Olson
Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from __future__ import print_function
import numpy as np
from sklearn.neighbors import KDTree


class ReliefF(object):
    def __init__(self, n_neighbors=100, n_features_to_keep=10):
	def fit(self, X, y):
        self.feature_scores = np.zeros(X.shape[1], dtype=np.int64)
        self.tree = KDTree(X)
        indices = self.tree.query(X, k=self.n_neighbors+1,
                                  return_distance=False)[:, 1:]
        for (source, nn) in enumerate(indices):
            labels_match = np.equal(y[source], y[nn]) * 2 - 1
            features_match = np.equal(X[source], X[nn]) * 2 - 1
            self.feature_scores += np.dot(features_match.T, labels_match)
        self.top_features = np.argsort(self.feature_scores)[::-1]
        self.feature_scores = self.feature_scores.astype(np.float64)
    def transform(self, X):
        return X[:, self.top_features[:self.n_features_to_keep]]
    def fit_transform(self, X, y):       
        self.fit(X, y)
        return self.transform(X)
x = np.loadtxt(r"e:\snp\res.csv",delimiter=",",usecols=range(9445),skiprows=0)  
y = np.loadtxt(r'e:\snp\phenotype.txt')
r = ReliefF()
RESULT = r.fit_transform(x,y)
score = r.feature_scores.tolist()
num = r.top_features.tolist()
f = open(r'e:\snp\ReliefF_Res2.txt','w')
ff = open(r'e:\snp\name.txt')
con = ff.readlines()[0]
name = con.split(' ')
for i in range(9445):
    f.write("%d,%s,%d\n"%(num[i],name[num[i]],score[num[i]]))
ff.close()
f.close()