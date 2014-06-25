#!/usr/bin/env python
import os,sys
from itertools import islice

##### classess #####

##### functions ####


def CigarStats(cig, r, r2):
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
    
        
    rstr = r.replace("'","").replace(",","").replace("]","")
    if rstr == "A":
        As = As + sames   
    if rstr == "T":
        Ts = Ts + sames
    if rstr == "C":
        Cs = Cs + sames
    if rstr == "G":
        Gs = Gs + sames
    total = As + Ts + Cs + Gs #+ sames
    
    if As >= 1:
        Aper = (float(As)/float(total))#*100
    else:
        Aper = 0
    if Ts >= 1:
        Tper = (float(Ts)/float(total))#*100
    else:
        Tper = 0
    if Cs >= 1:    
        Cper= (float(Cs)/float(total))#*100
    else:
        Cper = 0
    if Gs >= 1:
        Gper = (float(Gs)/float(total))#*100
    else:
	    Gper = 0
    
    
    bases = {'A' : As, 'T' : Ts, 'C' : Cs, 'G' : Gs} #'RefBase' : sames}
    maxBase = max(bases.iterkeys(), key=(lambda key: bases[key]))
    
    #return As,Ts,Cs,Gs,sames, total
    #return maxBase
    
    cons_bases = []
    if Aper >= baseThresh:
        cons_bases.append("A")
    if Tper >= baseThresh:
        cons_bases.append("T")
    if Cper >= baseThresh:
        cons_bases.append("C")
    if Gper >= baseThresh:
        cons_bases.append("G")
        
    #return Aper, Tper, Cper, Gper, cons_bases
	#return cons_bases   
	
    score = 0		
    CG_consSet = set()
    for i in cons_bases:
        CG_consSet.add(i)
    for i2 in r2:
        if i2 in CG_consSet:
            score = score + 1
        else:
            score = score
    score1 = 0
    if score > 0:
        score1 = 1
    else:
        score1 = score

    return cons_bases, score1



##### body #####


target_file = sys.stdin  # output from NS_redvar
baseThreshargv = sys.argv[1]
baseThresh = float(baseThreshargv)

totalScorePositionsSet = set()
totalScore = 0
totalpositions = 0

ref_bases = sys.argv[2]
ref_base = ref_bases[0]
refbase = int(ref_base)
ref_basesLen = len(ref_bases)

  
for line in target_file:
    l = line.split("\t")
    gene_pos = l[0]
    align_pos = l[1]
    group_bases = l[2]
    xgb = [s.strip() for s in group_bases[1:-1].split(',')]
    ref_basesList = []
    for i in range(ref_basesLen):
        ref_basesList.append(xgb[int(ref_bases[i])].replace("'","").replace(",","").replace("]",""))		
    pilup = l[3]
    #print pilup
    if pilup[:2] != "NA":
        p = pilup.split(" ")
        ppos = p[0]
        p_ref = xgb[refbase]
        if p_ref == "'.'":
		    p_ref = xgb[0]
        if p_ref != "'-'":
            p_cig = p[2]
            max_base, match_score = CigarStats(p_cig, p_ref, ref_basesList)
            if ppos not in totalScorePositionsSet:
                totalScore = totalScore + match_score
                totalpositions = totalpositions + 1
            totalScorePositionsSet.add(ppos)
            #print line.replace("\n",""), ppos, p_ref, max_base, match_score, ref_basesList
        
match_percent = 100 * (float(totalScore)/float(totalpositions))
print "\t", totalScore, "\t", totalpositions, "\t", match_percent, "%"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
