#!/usr/bin/env python
import sys,operator
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import itertools
import operator
from Bio import SeqIO

target = sys.stdin #open(sys.argv[1], "r")

seqs = []

for record in SeqIO.parse(target, "fastq"):
    length = len(record.seq)
    seqs.append(length)

#for line in target:
#	if line[0] != ">":
#		length = len(line)
#		seqs.append(length)
		
#print seqs

v = sum(seqs)
average = v / len(seqs)
m = max(seqs)

total = str(v)
mean = str(average)
top = str(m)

median = numpy.median(seqs)
median1 = str(median)
n = len(seqs)

nstr = str(n)

print "number of sequences: " + nstr 
print "total bases are: " + total 
print "average read length is: " + mean
print "longest read is: " + top
print "median read value is: " + median1

x = seqs
mu, sigma = m, 15

# the histogram of the data
n, bins, patches = plt.hist(x, 50, facecolor='green', alpha=0.75)

# add a 'best fit' line
#y = mlab.normpdf( bins, mu, sigma)
#l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('read length (bp)')
plt.ylabel('number of reads')
plt.title(r'Histogram of read length')
#plt.axis([0, m, 0, 15000])
plt.grid(True)

plt.show()
plt.savefig('histogram.png', format='png')

