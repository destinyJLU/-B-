# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:15:10 2016
@author: Administrator
"""
f = open(r'e:\snp\name.txt')
con = f.readlines()
for line in con:
    names = line.split(' ')
f.close()
import numpy as np  
X = np.loadtxt(r"e:\snp\res.csv",delimiter=",",usecols=range(0,9445),skiprows=0)  
array = X.tolist()
Y = np.loadtxt(r'e:\snp\multi_phenos.txt',delimiter=" ",usecols=range(0,10),skiprows=0)
y = Y.tolist()
ff = open(r'e:\snp\10_p_value.txt','w')
for q in range(0,10):
    p1 = [] #AA/Aa/aa
    p2 = [] #AA+Aa/aa
    p3 = [] #AA/Aa+aa
    p4 = [] #A/a
    for i in range(0,9445):
        d = 0
        e = 0
        f = 0    
        a = 0
        b = 0
        c = 0
        for j in range(0,1000):
            if array[j][i] == 0.0:
                if y[j][q]==0:
                    d += 1
                else:
                    a += 1
            elif array[j][i] == 1.0:
                if y[j][q]==0:
                    e += 1
                else:
                    b += 1
            elif array[j][i] == 2.0:
                if y[j][q]==0:
                    f += 1
                else:
                    c += 1
        EA = (a + d)/2.0
        EB = (b + e)/2.0
        EC = (c + f)/2.0
        k = ((a-EA)**2+(d-EA)**2)/EA*1.0 + ((b-EB)**2+(e-EB)**2)/EB*1.0 + ((c-EC)**2+(f-EC)**2)/EC*1.0
        p1.append([k,names[i],i])
        EA = (a+b+d+e)/2.0
        EB = (c+f)/2.0
        k = ((a+b-EA)**2+(d+e-EA)**2)/EA*1.0 + ((c-EB)**2+(f-EB)**2)/EB*1.0
        p2.append([k,names[i],i])    
        EA = (a+d)/2.0
        EB = (b+c+e+f)/2.0
        k = ((a-EA)**2+(d-EA)**2)/EA*1.0 + ((b+c-EB)**2+(e+f-EB)**2)/EB*1.0    
        p3.append([k,names[i],i])   
        EA = (2*a+b+2*d+e)/2.0
        EB = (2*c+b+2*f+e)/2.0
        k = ((2*a+b-EA)**2+(2*d+e-EA)**2)/EA*1.0 + ((2*c+b-EB)**2 + (2*f+e-EB)**2)/EB*1.0
        p4.append([k,names[i],i])
    ff.write("the %d th xingzhuang:\n"%(q+1))   
    p1.sort()
    p2.sort()
    p3.sort()
    p4.sort()
    ff.write("the p1 values are:\n")
    for (i,j,k) in p1:
        if i>13.81 :
            ff.write("%s,%s,%s\n"% (i,j,k))    
    ff.write("the p2 values are:\n")
    for (i,j,k) in p2:
       if i>10.83 :
            ff.write("%s,%s,%s\n"% (i,j,k))   
    ff.write("the p3 values are:\n")
    for (i,j,k) in p3:
        if i>10.83:
            ff.write("%s,%s,%s\n"% (i,j,k))    
    ff.write("the p4 values are:\n")
    for (i,j,k) in p4:
        if i>10.83:
            ff.write("%s,%s,%s\n"% (i,j,k))        
ff.close()