#!/usr/bin/env python
from __future__ import division
import sys,operator
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import itertools
import operator

baseline = sys.argv[1]
target = sys.argv[2]
bedfile = open(sys.argv[3], "r")
ratio = 1

def rangeDepth(start,stop,bfile):
    depths = []
    for line in open(bfile):
        l = line.split("\t")
        l_pos = int(l[-2])
        l_dep = int(l[-1])
        if l_pos > start:
            depths.append(l_dep)
    return depths

def compareRangeDepths(r1,r2):
    rN = len(r1)
    ratios = []
    z = 0
    for i in range(rN):
        if r2[i] == 0:
            ratios.append(1)
        elif r1[i] == 0:
            ratios.append(0)
            z = z + 1
        else:
            rR = r1[i] / float(r2[i])
            rR2 = rR / float(ratio)
            ratios.append(rR2)
    rTot = sum(ratios)
    rAve = rTot/rN
    return rAve, ratios

# fcar_start = 328544 - 894
# fcar_stop = 339141 - 894

fcar_start = 325000 - 894
fcar_stop = 366146 - 894


baseDepth = rangeDepth(fcar_start,fcar_stop,baseline)
targetDepth = rangeDepth(fcar_start,fcar_stop,target)


ratio, ratios = compareRangeDepths(targetDepth,baseDepth)
#print ratio

for line in bedfile:
    bed = line.split("\t")
    exonstart = int(bed[-2])
    exonstop = int(bed[-1])
    basexon = rangeDepth(exonstart,exonstop,baseline)
    tarexon = rangeDepth(exonstart,exonstop,target)
    exonratio, exonratios = compareRangeDepths(tarexon,basexon)
    #exonCNV = exonratio / ratio
    #print bed[3], exonratio, exonCNV
    
for i in exonratios:
    print i
   
    