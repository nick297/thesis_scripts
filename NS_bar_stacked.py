#!/usr/bin/env python
# a stacked bar plot 
import numpy as np
import matplotlib.pyplot as plt
import sys

############## functions ######################

def reorderElements(toReOrder, order):
    mylist = toReOrder
    #myorder=[3,2,0,1,4]
    mylist = [ mylist[i] for i in order]
    return mylist

def parse_output_file(file): ##### parse file and return lists of values
    tp_list = []
    pc_list = []
    for line in open(file, "r"):
        l = line.split("\t")
        if l[0] == "":
            tp = int(l[1])       # total positions
            pc = int(l[2])       # positions compared
            tp_list.append(tp)
            pc_list.append(pc)
    return tp_list, pc_list

############ gets files and parse them to lists #########
S1 = sys.argv[1]  # 100% coverage file
S2 = sys.argv[2]  # 75% coverage file
S3 = sys.argv[3]  # 50% coverage file
S4 = sys.argv[4]  # 25% coverage file    
score1_list, score1_pc = parse_output_file(S1)
score75_list, score75_pc = parse_output_file(S2)
score50_list, score50_pc = parse_output_file(S3)
score25_list, score25_pc = parse_output_file(S4)


##### stock lists

totala = np.array([791, 694, 791,76, 694, 76, 239, 556,\
239, 437, 556, 437, 713, 652, 713, 41, 652, 41, 156, 156, 510, 510])
genes = ('3DXL3 vs 3DXL5',\
'3DXL3 vs 3DXL7',\
'3DXL5 vs 3DXL3',\
'3DXL5 vs 3DXL7',\
'3DXL7 vs 3DXL3',\
'3DXL7 vs 3DXL5',\
'3DXL2 vs 3DXL4',\
'3DXL2 vs 3DXL6',\
'3DXL4 vs 3DXL2',\
'3DXL4 vs 3DXL6',\
'3DXL6 vs 3DXL2',\
'3DXL6 vs 3DXL4',\
'2DS1 vs 2DS2',\
'2DS1 vs 2DS3',\
'2DS2 vs 2DS1',\
'2DS2 vs 2DS3',\
'2DS3 vs 2DS1',\
'2DS3 vs 2DS2',\
'3DXS2 vs 3DXS3',\
'3DXS3 vs 3DXS2',\
'3DXL1 vs 3DSX1',\
'3DXS1 vs 3DLX1')

hapOrder = ([\
11,\
10,\
17,\
16,\
19,\
5,\
4,\
9,\
8,\
15,\
14,\
18,\
3,\
2,\
7,\
6,\
13,\
12,\
1,\
0,\
21,\
20,\
])

############ reorder elements of lists to haplotype order #############

genesR = reorderElements(genes,hapOrder)
score1_listR = reorderElements(score1_list,hapOrder)
score75_listR = reorderElements(score75_list,hapOrder)
score50_listR = reorderElements(score50_list,hapOrder)
score25_listR = reorderElements(score25_list,hapOrder)
score1_pcR = reorderElements(score1_pc,hapOrder)
totalaR = reorderElements(totala,hapOrder)

################## process lists so that can be shown in chart ##############

N = 22
score1a = np.array(score1_listR)
score75a = np.array(score75_listR)
score50a = np.array(score50_listR)
score25a = np.array(score25_listR)
compareda = np.array(score1_pcR)




####### subtract other lists so that stacked makes sense
score75 = score75a - score1a
score50 = score50a - (score1a + score75)
score25 = score25a - (score1a + score75 + score50)
compared = compareda - (score1a + score75 + score50)
total = totalaR - (score1a + score75 + score50  + compared)



############### create chart #################
ind = np.arange(N)    # the x locations for the groups
width = 0.50       # the width of the bars: can also be len(x) sequence
ax = plt.subplot2grid((12,6), (0,0), rowspan=9, colspan=5)

p1 = ax.bar(ind, score1a,   width, color='k', label='100%\ncuttoff')
p2 = ax.bar(ind, score75, width, color='0.25', bottom=score1a, label='75%\ncuttoff')
p3 = ax.bar(ind, score50, width, color='0.5', bottom=score1a + score75, label='50%\ncuttoff')
p4 = ax.bar(ind, compared, width, color='r', bottom=score1a + score75 + score50, label='Miss\nseq')
p5 = ax.bar(ind, total, width, color='0.99', bottom=score1a + score75 + score50 + compared, label='No\nseq.')

title = str(sys.argv[6])
savename = str(sys.argv[5])

ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':11})

plt.ylabel('SNP positions')
plt.title(title)
plt.xlim([0,score75.size])
plt.xticks(ind+width/2., (genesR), rotation=90)
#plt.yticks(np.arange(0,81,10))
#plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

#plt.show()
plt.savefig(savename, format='pdf')