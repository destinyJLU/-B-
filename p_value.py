#calculate p_value
f = open(r'e:\snp\name.txt')
con = f.readlines()
for line in con:
    names = line.split(' ')
import numpy as np  
X = np.loadtxt(r"e:\snp\res.csv",delimiter=",",usecols=range(0,9445),skiprows=0)  
array = X.tolist()
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
            if j<500:
                d += 1
            else:
                a += 1
        elif array[j][i] == 1.0:
            if j<500:
                e += 1
            else:
                b += 1
        elif array[j][i] == 2.0:
            if j<500:
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
p1.sort()
p2.sort()
p3.sort()
p4.sort()
f = open(r'e:\snp\p_value.txt','w')
f.write("the p1 values are:\n")
for (i,j,k) in p1:
    if i>13.81 :
        f.write("%s,%s,%s\n"% (i,j,k))
f.write("the p2 values are:\n")
for (i,j,k) in p2:
   if i>10.83 :
        f.write("%s,%s,%s\n"% (i,j,k))
f.write("the p3 values are:\n")
for (i,j,k) in p3:
    if i>10.83:
        f.write("%s,%s,%s\n"% (i,j,k))
f.write("the p4 values are:\n")
for (i,j,k) in p4:
    if i>10.83:
        f.write("%s,%s,%s\n"% (i,j,k))        
f.close()
