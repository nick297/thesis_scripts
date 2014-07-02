#!/usr/bin/env python
import sys
from Bio import SeqIO

target = sys.argv[1]
kmer = int(sys.argv[2])
overlap = int(sys.argv[3])

class seqArt:
    """artificial fragment format"""
    def __init__(self, fr, qu, nam):
        self.n = nam
        self.s = fr
        self.q = qu

qual_list = []
for q in range(kmer):
    qual_list.append("@")

frag_qual = "".join(qual_list)

def chop(sequence, name, length):
    seqLength = int(len(sequence))
    n_start = 0
    n_stop = length
    seq_list = []
    while n_stop < seqLength:
        fragment = sequence[n_start:n_stop]
        frag_name = name + "_" + str(n_start) + ":" + str(n_stop)
        n_start = n_start + overlap
        n_stop = n_stop + overlap
        x = seqArt(fragment, frag_qual, frag_name)
        seq_list.append(x)
    return seq_list


for seqrecord in SeqIO.parse(target, "fasta"):
    frag_list = chop(str(seqrecord.seq), str(seqrecord.id), int(kmer))
    for i in frag_list:
        print "@" + i.n + "_pos"
        print i.s
        print "+"
        print i.q
    frag_list_RC = chop(str(seqrecord.seq.reverse_complement()), str(seqrecord.id), int(kmer))
    for i in frag_list_RC:
        print "@" + i.n + "_neg"
        print i.s
        print "+"
        print i.q
