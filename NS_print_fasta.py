#!/usr/bin/env python
import sys
from Bio import SeqIO
import os
import gzip


FastaFile = gzip.open(sys.argv[1], 'r')

#FastaFile = sys.stdin
record = SeqIO.read(FastaFile, "fasta")

print ">" + record.id

#print record.seq[0:32200000]  #### Chrom X start to KIR
#print record.seq[40200000:-1] #### Chrom X KIR to finish
#print record.seq[0:62803000]    ### Chrom 18 start to KIR
                   #62827511
#print record.seq[63376971:-1]    #### Chrom 18 KIR to finish
#print record.seq[0:86738157] ### Chrom 4 start to KIR
#86738157
#print record.seq[86743206:-1]    #### Chrom 4 KIR to finish
#86743206

#print record.seq[0:32536223] ### Chrom 10 start to KIR
#32536223
#print record.seq[32537684:-1]    #### Chrom 10 KIR to finish
#print record.seq[0:47062595] ### Chrom 1 start to KIR

#print record.seq[47063187:-1]    #### Chrom 1 KIR to finish

#print record.seq[0:7385944] ### Chrom 26 start to KIR
#print record.seq[7387216:31584892]
#print record.seq[31592428:-1]  #### Chrom 26 KIR to finish