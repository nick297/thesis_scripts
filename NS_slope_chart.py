#!/usr/bin/env python
import sys,operator
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

target = sys.argv[1]

bwa1 = []
bwa2 = []
bwa3 = []
bwa4 = []
fragment = []

for line in open(target, "r"):
    l = line.split("\t")
    if line[0] != "#":
        bwa1.append(float(l[0]))
        bwa2.append(float(l[1]))
        bwa3.append(float(l[2]))
        bwa4.append(float(l[3]))
        fragment.append(float(l[4]))
    else:
        bwa1_label = str(l[0]).replace("#","")
        bwa2_label = str(l[1])
        bwa3_label = str(l[2])
        bwa4_label = str(l[3]).replace("\n","")
        fragment_label = str(l[3]).replace("\n","")

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(fragment, bwa1, 'k-', label=bwa1_label)
ax1.plot(fragment, bwa2, 'r-', label=bwa2_label)
ax1.plot(fragment, bwa3, 'b-', label=bwa3_label)
ax1.plot(fragment, bwa4, 'g-', label=bwa4_label)
ax1.legend(loc=4)
plt.xlim(0,1200.0)
plt.ylim(40,102.0)
ax1.set_xlabel('Fragment size (bp)')
ax1.set_ylabel('Breadth of coverage (%)')

#plt.show()
plt.savefig("slope.pdf")