#!/usr/bin/env python
import sys,operator
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import itertools
import operator



target = open(sys.argv[1], "r")
filename = sys.argv[1]
slidWindow = int(sys.argv[2])
fileSaveName = filename.replace(".bed", "")

illumina = []
illuminaMean= []
#roche = []

r = slidWindow
rstart = 0 + r
rstop = 370114 - r

def dynamicRange(n): ## upSet is up range of n ## downSet is down range of n
	ni = n -1
	upN = ni + r
	downN = ni - r
	dRange = []
	x = downN + 1
	#dRcov = 0
	while x > downN and x < upN:
			dRcov = illumina[x]
			dRcovInt = int(dRcov)
			dRange.append(dRcovInt) #.replace("\n",""))
			x = x + 1
	dRmean = np.mean(dRange)
	return dRmean
	
#	downNstr = str(downN)
#	nistr = str(ni)
#	upNstr = str(upN)
#	return downNstr + "\t" + nistr + "\t" + upNstr #.replace("\n","")
	
	
for line in target:
	l = line.split("\t")
	illCov = l[5]
	#illCovInt = int(illCov) #.replace("\n",""))
	illumina.append(illCov)#Int) 

target = open(sys.argv[1], "r")

for line in target:
	l = line.split("\t")
	pos = l[4]
	posInt = int(pos)
	if posInt > rstart:
		if posInt < rstop:
			dynrangeStats = dynamicRange(posInt)
			dynrangeStatsInt = int(dynrangeStats)
			illuminaMean.append(dynrangeStatsInt)
	#illuminaMean.append(dynrangeStats)
	
for i in illuminaMean:
    print i

####### matplotlib part to make graph ######
rValue = str(r)
fileSaveName = filename.replace(".bed", "") + "_R" + rValue

fig = plt.figure(figsize=(16,9))
ax1 = fig.add_subplot(111)
t = np.arange(0.01, 10.0, 0.01)
s1 = illuminaMean #np.exp(t)
ax1.plot(s1, 'r-')
ax1.set_xlabel('pos (bp)')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('illumina coverage (x reads)', color='k')
#ax1.axvspan(50000, 70000,facecolor='gray')
#ax1.axvspan(80000, 90000,facecolor='gray')
plt.title(fileSaveName)
## axis range ##

ax1.axis([0.0,375000.0, 0.0,200.0])
ax1.set_autoscale_on(False)



########### KIR regions #########################
ax1.axvspan(62076,69141,facecolor='gray')#	3DXL6
ax1.axvspan(71580,77407,facecolor='gray')#	2DS3
ax1.axvspan(82174,87568,facecolor='gray')#	3DXS3
ax1.axvspan(97731,107326,facecolor='gray')#	3DXL7
ax1.axvspan(132747,140360,facecolor='gray')#	3DXL4
ax1.axvspan(144211,150034,facecolor='gray')#	2DS2
ax1.axvspan(154794,160963,facecolor='gray')#	3DXS2
ax1.axvspan(170279,179882,facecolor='gray')#	3DXL5
ax1.axvspan(205374,212910,facecolor='gray')#	3DXL2
ax1.axvspan(214470,222555,facecolor='gray')#	2DS1
ax1.axvspan(230427,242938,facecolor='gray')#	3DXL3
ax1.axvspan(273824,279418,facecolor='gray')#	3DXS1
ax1.axvspan(304526,312244,facecolor='gray')#	3DXL1
ax1.axvspan(313914,323934,facecolor='gray')#	2DL1
#ax1.axvspan.set_colour('r')
for tl in ax1.get_yticklabels():
    tl.set_color('k')


#plt.savefig(fileSaveName)  

plt.show()
