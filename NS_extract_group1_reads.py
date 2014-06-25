#!/usr/bin/env python
## script to print all lines except ones containing 
## usage on aln.sam
## 

import sys

target = open(sys.argv[1], 'r')

######################## group sets #################################

group1 = set()
group2 = set()
group3 = set()
groupMISC = set()

group1.add('seq7')
group1.add('seq14')

group2.add('seq8')
group2.add('seq10')
group2.add('seq12')

group3.add('seq9')
group3.add('seq11')
group3.add('seq13')

groupMISC.add('seq1')
groupMISC.add('seq2')
groupMISC.add('seq3')
groupMISC.add('seq4')
groupMISC.add('seq5')
groupMISC.add('seq6')
groupMISC.add('seq15')
groupMISC.add('seq16')
groupMISC.add('seq17')
groupMISC.add('seq18')

groupMISC.add('gi|257481335|tpg|GK000010.2|')
groupMISC.add('gi|257481334|tpg|GK000011.2|')
groupMISC.add('gi|257481333|tpg|GK000012.2|')
groupMISC.add('gi|257481332|tpg|GK000013.2|')
groupMISC.add('gi|257481331|tpg|GK000014.2|')
groupMISC.add('gi|257481330|tpg|GK000015.2|')
groupMISC.add('gi|257481329|tpg|GK000016.2|')
groupMISC.add('gi|257481328|tpg|GK000017.2|')
groupMISC.add('gi|257481327|tpg|GK000018.2|')
groupMISC.add('gi|257481326|tpg|GK000019.2|')
groupMISC.add('gi|257481614|tpg|GK000001.2|')
groupMISC.add('gi|257481325|tpg|GK000020.2|')
groupMISC.add('gi|257481324|tpg|GK000021.2|')
groupMISC.add('gi|257481323|tpg|GK000022.2|')
groupMISC.add('gi|257481322|tpg|GK000023.2|')
groupMISC.add('gi|257481321|tpg|GK000024.2|')
groupMISC.add('gi|257481320|tpg|GK000025.2|')
groupMISC.add('gi|257481319|tpg|GK000026.2|')
groupMISC.add('gi|257481318|tpg|GK000027.2|')
groupMISC.add('gi|257481317|tpg|GK000028.2|')
groupMISC.add('gi|257481316|tpg|GK000029.2|')
groupMISC.add('gi|257481613|tpg|GK000002.2|')
groupMISC.add('gi|257481612|tpg|GK000003.2|')
groupMISC.add('gi|257481341|tpg|GK000004.2|')
groupMISC.add('gi|257481340|tpg|GK000005.2|')
groupMISC.add('gi|257481339|tpg|GK000006.2|')
groupMISC.add('gi|257481338|tpg|GK000007.2|')
groupMISC.add('gi|257481337|tpg|GK000008.2|')
groupMISC.add('gi|257481336|tpg|GK000009.2|')
groupMISC.add('gi|346683397|gb|CM000206.4|')


######################## not in Group sets #####################################

nongroup1 = set()
nongroup2 = set()
nongroup3 = set()
nongroupMISC = set()

#group1.add('seq7')
#group1.add('seq14')

nongroup1.add('seq8')
nongroup1.add('seq10')
nongroup1.add('seq12')

nongroup1.add('seq9')
nongroup1.add('seq11')
nongroup1.add('seq13')

nongroup1.add('seq1')
nongroup1.add('seq2')
nongroup1.add('seq3')
nongroup1.add('seq4')
nongroup1.add('seq5')
nongroup1.add('seq6')
nongroup1.add('seq15')
nongroup1.add('seq16')
nongroup1.add('seq17')
nongroup1.add('seq18')

nongroup1.add('gi|257481335|tpg|GK000010.2|')
nongroup1.add('gi|257481334|tpg|GK000011.2|')
nongroup1.add('gi|257481333|tpg|GK000012.2|')
nongroup1.add('gi|257481332|tpg|GK000013.2|')
nongroup1.add('gi|257481331|tpg|GK000014.2|')
nongroup1.add('gi|257481330|tpg|GK000015.2|')
nongroup1.add('gi|257481329|tpg|GK000016.2|')
nongroup1.add('gi|257481328|tpg|GK000017.2|')
nongroup1.add('gi|257481327|tpg|GK000018.2|')
nongroup1.add('gi|257481326|tpg|GK000019.2|')
nongroup1.add('gi|257481614|tpg|GK000001.2|')
nongroup1.add('gi|257481325|tpg|GK000020.2|')
nongroup1.add('gi|257481324|tpg|GK000021.2|')
nongroup1.add('gi|257481323|tpg|GK000022.2|')
nongroup1.add('gi|257481322|tpg|GK000023.2|')
nongroup1.add('gi|257481321|tpg|GK000024.2|')
nongroup1.add('gi|257481320|tpg|GK000025.2|')
nongroup1.add('gi|257481319|tpg|GK000026.2|')
nongroup1.add('gi|257481318|tpg|GK000027.2|')
nongroup1.add('gi|257481317|tpg|GK000028.2|')
nongroup1.add('gi|257481316|tpg|GK000029.2|')
nongroup1.add('gi|257481613|tpg|GK000002.2|')
nongroup1.add('gi|257481612|tpg|GK000003.2|')
nongroup1.add('gi|257481341|tpg|GK000004.2|')
nongroup1.add('gi|257481340|tpg|GK000005.2|')
nongroup1.add('gi|257481339|tpg|GK000006.2|')
nongroup1.add('gi|257481338|tpg|GK000007.2|')
nongroup1.add('gi|257481337|tpg|GK000008.2|')
nongroup1.add('gi|257481336|tpg|GK000009.2|')
nongroup1.add('gi|346683397|gb|CM000206.4|')

nongroup2.add('seq7')
nongroup2.add('seq14')

#nongroup2.add('seq8')
#nongroup2.add('seq10')
#nongroup2.add('seq12')

nongroup2.add('seq9')
nongroup2.add('seq11')
nongroup2.add('seq13')

nongroup2.add('seq1')
nongroup2.add('seq2')
nongroup2.add('seq3')
nongroup2.add('seq4')
nongroup2.add('seq5')
nongroup2.add('seq6')
nongroup2.add('seq15')
nongroup2.add('seq16')
nongroup2.add('seq17')
nongroup2.add('seq18')

nongroup2.add('gi|257481335|tpg|GK000010.2|')
nongroup2.add('gi|257481334|tpg|GK000011.2|')
nongroup2.add('gi|257481333|tpg|GK000012.2|')
nongroup2.add('gi|257481332|tpg|GK000013.2|')
nongroup2.add('gi|257481331|tpg|GK000014.2|')
nongroup2.add('gi|257481330|tpg|GK000015.2|')
nongroup2.add('gi|257481329|tpg|GK000016.2|')
nongroup2.add('gi|257481328|tpg|GK000017.2|')
nongroup2.add('gi|257481327|tpg|GK000018.2|')
nongroup2.add('gi|257481326|tpg|GK000019.2|')
nongroup2.add('gi|257481614|tpg|GK000001.2|')
nongroup2.add('gi|257481325|tpg|GK000020.2|')
nongroup2.add('gi|257481324|tpg|GK000021.2|')
nongroup2.add('gi|257481323|tpg|GK000022.2|')
nongroup2.add('gi|257481322|tpg|GK000023.2|')
nongroup2.add('gi|257481321|tpg|GK000024.2|')
nongroup2.add('gi|257481320|tpg|GK000025.2|')
nongroup2.add('gi|257481319|tpg|GK000026.2|')
nongroup2.add('gi|257481318|tpg|GK000027.2|')
nongroup2.add('gi|257481317|tpg|GK000028.2|')
nongroup2.add('gi|257481316|tpg|GK000029.2|')
nongroup2.add('gi|257481613|tpg|GK000002.2|')
nongroup2.add('gi|257481612|tpg|GK000003.2|')
nongroup2.add('gi|257481341|tpg|GK000004.2|')
nongroup2.add('gi|257481340|tpg|GK000005.2|')
nongroup2.add('gi|257481339|tpg|GK000006.2|')
nongroup2.add('gi|257481338|tpg|GK000007.2|')
nongroup2.add('gi|257481337|tpg|GK000008.2|')
nongroup2.add('gi|257481336|tpg|GK000009.2|')
nongroup2.add('gi|346683397|gb|CM000206.4|')

nongroup3.add('seq7')
nongroup3.add('seq14')

nongroup3.add('seq8')
nongroup3.add('seq10')
nongroup3.add('seq12')

#nongroup3.add('seq9')
#nongroup3.add('seq11')
#nongroup3.add('seq13')

nongroup3.add('seq1')
nongroup3.add('seq2')
nongroup3.add('seq3')
nongroup3.add('seq4')
nongroup3.add('seq5')
nongroup3.add('seq6')
nongroup3.add('seq15')
nongroup3.add('seq16')
nongroup3.add('seq17')
nongroup3.add('seq18')

nongroup3.add('gi|257481335|tpg|GK000010.2|')
nongroup3.add('gi|257481334|tpg|GK000011.2|')
nongroup3.add('gi|257481333|tpg|GK000012.2|')
nongroup3.add('gi|257481332|tpg|GK000013.2|')
nongroup3.add('gi|257481331|tpg|GK000014.2|')
nongroup3.add('gi|257481330|tpg|GK000015.2|')
nongroup3.add('gi|257481329|tpg|GK000016.2|')
nongroup3.add('gi|257481328|tpg|GK000017.2|')
nongroup3.add('gi|257481327|tpg|GK000018.2|')
nongroup3.add('gi|257481326|tpg|GK000019.2|')
nongroup3.add('gi|257481614|tpg|GK000001.2|')
nongroup3.add('gi|257481325|tpg|GK000020.2|')
nongroup3.add('gi|257481324|tpg|GK000021.2|')
nongroup3.add('gi|257481323|tpg|GK000022.2|')
nongroup3.add('gi|257481322|tpg|GK000023.2|')
nongroup3.add('gi|257481321|tpg|GK000024.2|')
nongroup3.add('gi|257481320|tpg|GK000025.2|')
nongroup3.add('gi|257481319|tpg|GK000026.2|')
nongroup3.add('gi|257481318|tpg|GK000027.2|')
nongroup3.add('gi|257481317|tpg|GK000028.2|')
nongroup3.add('gi|257481316|tpg|GK000029.2|')
nongroup3.add('gi|257481613|tpg|GK000002.2|')
nongroup3.add('gi|257481612|tpg|GK000003.2|')
nongroup3.add('gi|257481341|tpg|GK000004.2|')
nongroup3.add('gi|257481340|tpg|GK000005.2|')
nongroup3.add('gi|257481339|tpg|GK000006.2|')
nongroup3.add('gi|257481338|tpg|GK000007.2|')
nongroup3.add('gi|257481337|tpg|GK000008.2|')
nongroup3.add('gi|257481336|tpg|GK000009.2|')
nongroup3.add('gi|346683397|gb|CM000206.4|')



################################ code ######################################################

def checkNAME(L):  ##### function to sort on how many hits (1-3)
	L1 = L.split('XA:Z:')
	L1b = L1[1]
	L2 = L1b.split(';')
	length = len(L2) - 1
	lengths = str(length)
	fz = nongroup1
	#print "length = " + lengths	
	if length == 1:
		hitBag = checkHITs1(L2, fz)
	if length == 2:
		hitBag = checkHITs2(L2, fz)
	if length == 3:
		hitBag = checkHITs3(L2, fz)
	if hitBag < 1:	
		print line.replace('\n', ',')
	

def checkHITs1(P, fzx):
	H1 = P[0]
	hit = H1.split(',')
	hit1 = hit[0]
	hit1str = str(hit1)
	if hit1str in fzx:
		return 1
	else:
		return 0
	
	
def checkHITs2(P, fzx):
	H1 = P[0]
	hit = H1.split(',')
	hit1 = hit[0]
	H2 = P[1]
	hit2 = H2.split(',')
	hit3 = hit2[0]
	hit1str = str(hit1)
	hit2str = str(hit3)
	n = 0
	if hit1str in fzx:
		n = n + 1
	if hit2str in fzx:
		n = n + 1
	return n

def checkHITs3(P, fzx):
	H1 = P[0]
	hit = H1.split(',')
	hit1 = hit[0]
	H2 = P[1]
	hit2 = H2.split(',')
	hit3 = hit2[0]
	H3 = P[2]
	hit4 = H3.split(',')
	hit5 = hit4[0]
	hit1str = str(hit1)
	hit2str = str(hit3)
	hit3str = str(hit5)
	n = 0
	if hit1str in fzx:
		n = n + 1
	if hit2str in fzx:
		n = n + 1
	if hit3str in fzx:
		n = n + 1
	return n

for line in target:
	if line[0] != '@':
		line1 = line.split('\t')
		chromTarget =  line1[2]
		if chromTarget in group1:
			if 'XA' in line:
				checkNAME(line)
			else:
				print line.replace('\n', ',')
	else:
		print line.replace('\n', ',')
