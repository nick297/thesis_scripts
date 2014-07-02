#!/usr/bin/env python
from matplotlib.pyplot import show
import sys
from hcluster import pdist, linkage, dendrogram
import numpy
from numpy.random import rand

fofn = sys.argv[1]

def getVals(file):
    v = []
    for line in open(file, "r"):
        v.append(int(line))
    return v

lables = []
AllVals = []
for files in open(fofn, "r"):
    f = files.split('\t')
    fileName = f[0]
    name = (f[1]).replace('\n','')
    Vals = getVals(fileName.replace('\n',''))
    AllVals.append(Vals)
    lables.append(name)
print AllVals

#X = rand(10,100)
X = AllVals
#X[0:5,:] *= 2
Y = pdist(X)
Z = linkage(Y)
dendrogram(Z,orientation='right',labels=lables,color_threshold=1860)

show()
