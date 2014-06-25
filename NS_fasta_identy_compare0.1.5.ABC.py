#!/usr/bin/env python
import sys
from Bio import SeqIO
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

target = sys.argv[1] # file containing aligned sequences
reference_sequence = int(sys.argv[2]) # base sequence for others to be compared to
windowSize1 = int(sys.argv[3]) # sliding windows base size
#windowSize = windowSize1 / 5

class similarityData:
    """data structure for similarity"""
    def __init__(self, name, refbase, seqbase, sscore, pos):
        self.n = name
        self.rb = refbase
        self.sb = seqbase
        self.sc = sscore
        self.p = pos
    

def compareSeqs(ids, seqs, ref): # function to calculate identity
    if ids != ref:
        n = 0
        total_list = []
        while n < len(ref):
            refb = ref[n]
            x_list = []
            for l in range(len(seqs)):
                i = ids[l]	
                seqi = ids[l]
                seqstr = seqs[l]
                seqb = seqstr[n]
                if refb == seqb:
                    score = 1		
                else:
                    score = 0
                x = similarityData(i, refb, seqb, score, n)
                x_list.append(int(x.sc))
                total_list.append(x_list)
            n = n + 1
    #print total_list	
        rawList = [sum(item) for item in zip(*total_list)]
        divider = len(seqs)
        myFloat = float(windowSize) * divider  #* len(ids)
        newList = [x/myFloat for x in rawList]   
        #print rawList
        return newList

def slidingWindow(begin, end):
    sequenceList = []
    sequenceIDs = []
    slidList = []
    for seqrecord in SeqIO.parse(target, 'fasta'):
        sequenceList.append(str(seqrecord.seq[begin:end]))
        sequenceIDs.append(str(seqrecord.id))
    RefSeq = sequenceList[reference_sequence]
    del sequenceList[reference_sequence]
    list1 = compareSeqs(sequenceIDs, sequenceList, RefSeq)
    #print list1
    del sequenceIDs[reference_sequence]
    return list1, sequenceIDs
    
lengths = []
bed_seqs = []
for seqrecord in SeqIO.parse(target, 'fasta'):
    lengths.append(len(seqrecord.seq))
    bed_seqs.append(seqrecord.seq)
    
bed_ref = bed_seqs[reference_sequence]
 
windowSize = windowSize1 / len(lengths)
e = windowSize

x_axis = []
all_lists = []
xa = 0
while e < min(lengths):
    list2,labels = slidingWindow((e - windowSize), e)  
    all_lists.append(list2)
    x_axis.append(xa)
    e = e + 1
    xa = xa + 1



################# code for generating the image 


#fig = plt.figure()
#ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])
ax = plt.subplot2grid((12,6), (1,0), rowspan=9, colspan=5)
s1 = all_lists
lable_len = len(labels) 

for i in range(10):
    print s1[i]


for p in range(lable_len):
    s = []
    q = p 
    lab = labels[p]
    for i in range(len(s1)):
        s2 = s1[i][q]
        s.append(s2)
    ax.plot(s, label=lab)
ax.set_xlabel('pos (bp)')
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.set_ylabel('Identity score')
ax.axis([0.0,min(lengths), 0.0,1.0])

################ Code for unique regions #########################
from itertools import groupby
from operator import itemgetter

def whichUnique(startGap, stopGap, TestSequence):
    gapScore = []
    for i in TestSequence[startGap:stopGap]:
        if i != '-':
            gapScore.append(1)
        else:
            gapScore.append(0)
    TotalScore = float(sum(gapScore)) / float(len(gapScore))
    if TotalScore > 0.2:
        return True
    else:
        return False


seqs = []
for seqrecord in SeqIO.parse(target, 'fasta'):
    seqs.append(seqrecord.seq)

ref_seq = seqs[reference_sequence]
e = 0
unique_area = []
while e < min(lengths):
    ref_base = ref_seq[e]
    if ref_base == '-':
        unique_area.append(e)
        stopper = ref_base
    e = e + 1
    
for k, g in groupby(enumerate(unique_area), lambda (i,x):i-x):
    gap = map(itemgetter(1), g)
    #print gap
    if len(gap) > windowSize1:
        String = ""
        start = gap[0]
        stop = gap[-1]
        middle = start + ((stop - start)/2)
        ax.axvspan(start,stop, ymin=0, ymax=1,ec='none', facecolor='0.85')#, alpha=0.5)
        for seqrecord in SeqIO.parse(target, 'fasta'):
            if whichUnique(start, stop, str(seqrecord.seq)) == True:
                String = String + str(seqrecord.id) + "\n"
        String = String.replace("_"," ").rstrip("\n")
        ax.annotate(String, xy=(middle, 0.), xytext=(middle, 1), ha='center' ,va='bottom', rotation=90, bbox=dict(boxstyle="round", fc="w"))




################ code for gene annototations ##########################

bedfile = sys.argv[4]
blockA = 0 # if annotation doesn't start at zero set it here  #289488
blockAFin = min(lengths) # same for the ending of the reference fasta # 325475
ax1 = plt.subplot2grid((12,6), (11,0), colspan=5)
ax1.axis([0.0,min(lengths), 0.0,1.0])
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
oldStart = "X"
oldStartexon ="X"



def count_pads(sequence, A):
    pads = 0
    nP = 0
    nA = A
    while nP < nA:
        if nP < min(lengths):
            if sequence[nP] == "-":
                pads = pads + 1
                nA = nA + 1
                nP = nP + 1	    
            else:
                nP = nP + 1	
        else:
            nP = nP + 1        		    
    return int(pads)
    #print pads

#print bed_ref

for line in open(bedfile):
    l = line.split("\t")
    start1 = int(l[1]) - blockA
    end1 = int(l[2]) - blockA
    if end1 < min(lengths):
        pads1 = int(count_pads(bed_ref, start1))
        start = start1 + pads1
    
        pads2 = (count_pads(bed_ref, end1))
        end = end1 + pads2
        gene_name2 = str(l[3]).split(" ")
        gene_name = gene_name2[0]
        middle = start + (int((end - start)/2))
        print pads1, start1, start, gene_name2
        blockA2 = blockA + pads1
        blockAFin2 = blockAFin + pads2
        if int(l[1]) < blockAFin:
            if int(l[1]) > blockA:
                if start != oldStart:
                    oldStart = start		
                    ax1.axvspan(start,end,facecolor='0.5')
                    ax1.annotate(gene_name, xy=(middle, -0.), xytext=(middle, -0.05), va='top', ha='center',  bbox=dict(boxstyle="round", fc="w")
                        )

for line in open(bedfile):
    l = line.split("\t")
    if int(l[-1]) < blockAFin:
        if (l[-2]) > blockA:

#### exons annotation ####
            start3 = int(l[-2]) - blockA
            start2 = start3 + int(count_pads(bed_ref, start3))
            end3 = int(l[-1]) - blockA
            end2 = end3 + (count_pads(bed_ref, end3))
    #### exons annotation over ####
            if start2 != oldStartexon:
                oldStartexon = start2
                ax1.axvspan(start2,end2,facecolor='k')



plt.show()









