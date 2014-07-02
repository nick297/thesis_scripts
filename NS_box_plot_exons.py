#!/usr/bin/env python
import sys,operator
import numpy
from Bio import SeqIO
from collections import Counter
from pylab import *

bedfile = sys.argv[1]
ratioFile = sys.argv[2]


def getRatios(eStart, eStop):
    n = 0
    rlist = []
    for i in open(ratioFile, 'r'):
        if n >= eStart:
            if n < eStop:
                rlist.append(float(i))
        n = n + 1
    return rlist

pops = []
names = []

rspan = 0
facecol = 1
prev = 0
for line in open(bedfile, 'r'):
    l = line.split("\t")
    exonstart = int(l[-2])
    exonstop = int(l[-1])
    ratios = getRatios(exonstart, exonstop)
    names.append(str(l[3]))
    pops.append(ratios)



fig = plt.figure(figsize=(16,8))
ax = plt.subplot2grid((16,8), (0,0), colspan=9, rowspan=10)    

ax.boxplot(pops)
labels = names
n = len(names) + 1
xticks(range(1,n),labels,rotation=90)
xlabel('Exon')
ylabel('Ratio to HF4222')
tick_params(axis='both', which='major', labelsize=8)
tick_params(axis='both', which='minor', labelsize=8)

titleName = ratioFile.lstrip('../')
ax.set_title(titleName.rstrip('.sorted.bam.bedratios.txt'))
     
axvspan(0,9.5,facecolor='0.8')
axvspan(16,22.5,facecolor='0.8')
axvspan(32,40.5,facecolor='0.8')
axvspan(47,53.5,facecolor='0.8')
axvspan(63,71.5,facecolor='0.8')
axvspan(63,71.5,facecolor='0.8')
axvspan(78,86.5,facecolor='0.8')
axvspan(94,102.5,facecolor='0.8')

#axvspan(0,7,facecolor='gray')#	3DXL6

savename = titleName.rstrip('.sorted.bam.bedratios.txt') + '_normalised_boxplots.pdf'
print savename

#plt.savefig(savename, format='pdf')
show()