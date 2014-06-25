#!/usr/bin/env python
import os,sys
from itertools import islice

##### classess #####

class seqStore:                      	## class for seq name and seq
    def __init__(self, seqname, seq):
        self.nm = seqname
        self.sq = seq


class varseqStore:                      	## class for seq name and seq
    def __init__(self, vseqname, vseq):
        self.vnm = vseqname
        self.vsq = vseq
        
class pileupClass:                      	## class for pilup seq name and ciagr
    def __init__(self, pgene, ppos, pcigar, pref):
        self.pg = pgene
        self.pp = int(ppos)
        self.pc = pcigar
        self.pr = pref

##### functions ####

def returnPos(pos):				## function to reurn list at position
    pos_list = []
    for t in name_list:
        pos_list.append(t.sq[pos])
    return pos_list
    
    
def all_same(items):
    return all(x == items[0] for x in items)



def checkPlup(cPpos):
    cPvalue = "NA"
    for i in pilupname_list:
        if i.pp == cPpos:
            cPvalue = i.pp, i.pr, i.pc
    return cPvalue    	


def CigarStats(cig):
    a = cig.count('a')
    t = cig.count('t')
    c = cig.count('c')
    g = cig.count('g')

    A = cig.count('A')
    T = cig.count('T')
    C = cig.count('C')
    G = cig.count('G')

    dots = cig.count('.')
    commas = cig.count(',')
    
    As = a + A
    Ts = t + T
    Cs = c + C
    Gs = g + G
    sames = dots + commas
    total = As + Ts + Cs + Gs + sames
    
    bases = {'A' : As, 'T' : Ts, 'C' : Cs, 'G' : Gs, 'RefBase' : sames}
    maxBase = max(bases.iterkeys(), key=(lambda key: bases[key]))
    
    #return As,Ts,Cs,Gs,sames, total
    return maxBase

def isItinteresting(bases):
    nBases = len(bases)
    dots = 0
    for i in bases:
        if i == "." or i == "-":
            dots = dots + 1
    if nBases - dots >= 2:
        return True
    else:
        return False	    		

##### body #####


csv_file = open(sys.argv[1],"r")	# csv output from mega



      		
with csv_file as myfile:			# open file and determine length of seq
    fline=list(islice(myfile,1)) 	# first line of file
    s = str(fline) 					# string forst line of file
    l = s.split(",")				# split fline by comma
    n = len(l)						# length of split 
    nline = int(n) - 3				# correct number
    


csv_file = open(sys.argv[1],"r")	# csv output from mega

name_list = []

for line in csv_file:
    if line[0] != ",":
        l = line.split(",")
        #print l[2:n]    	
        name = l[0]
        sequence = l[2:]
        name = seqStore(name,sequence)
        name_list.append(name)
        
uN = 0 			# unique number

for i in range(nline):
    positions = returnPos(i)
    if all_same(positions) == False: ### only print positions with sequence
        #print i, uN, positions		
        uN = uN + 1

### pilup data

   	
pileup_file = open(sys.argv[2],"r")	#       

pilupname_list = []

for line in pileup_file:
    l = line.split("\t")
    pil_gene = l[0]
    pil_pos = l[1]
    pil_ref = l[2]
    pil_nseqs = l[3]
    pil_cigar = l[4]
    pil_name = str(pil_pos)
    pil_name = pileupClass(pil_gene, pil_pos, pil_cigar, pil_ref)
    pilupname_list.append(pil_name)
    
#for i in pilupname_list:
#    print i, i.pp, i.pc
    
##### combined ###
uN = 1

inarg = int(sys.argv[3])

for i in range(nline):
    positions = returnPos(i)
    plup_value = checkPlup(uN)
    #if all_same(positions) == False: ### only print positions with sequence
    if positions[inarg] != "-":
        uN = uN + 1
    if isItinteresting(positions) == True:
        print i,"\t", uN,"\t", positions,"\t", plup_value
            	
