#!/usr/bin/env python
from Bio import SeqIO
import sys
import os

target = sys.argv[1]

lines = []
size = 76887
for i in range(size):
    lines.append("-")



for record in SeqIO.parse(target, "fasta") :
    print ">" + str(record.id)
    print "".join(lines)
    print record.seq
