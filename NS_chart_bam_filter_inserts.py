#!/usr/bin/env python
import sys,operator
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import itertools
import operator
import pysam
from matplotlib.widgets import SpanSelector

target = sys.argv[1]
samfile = pysam.Samfile(target, "rb" )
threshold = str(sys.argv[2])
thresh = threshold.split("-")
thresh1 = int(thresh[0])
thresh2 = int(thresh[1])

mthresh1 = thresh1 * -1
mthresh2 = thresh2 * -1

#print mthresh1

chromosome = samfile.references[0]
f1 = samfile.lengths[0]

filtered_samfile = pysam.Samfile(".filtered_bam", "wb", template=samfile)
for alignedread in samfile.fetch(chromosome, 0, f1):
    insert_size = alignedread.isize
    if insert_size >= thresh1 and insert_size <= thresh2:
        filtered_samfile.write(alignedread)
    if insert_size >= mthresh2 and insert_size <= mthresh1:
        filtered_samfile.write(alignedread)

filtered_samfile.close()
samfile.close()


#samfile = pysam.Samfile(".filtered_bam", "r")
pysam.sort(".filtered_bam", ".filtered_sorted")
pysam.index(".filtered_sorted.bam")
samfile = pysam.Samfile(".filtered_sorted.bam", "rb")
cov = []
overThreshCov = []
pos = []

posN = 0
for pileupcolumn in samfile.pileup(chromosome, 0, f1, max_depth=1000000):
    position = pileupcolumn.pos
    coverage = pileupcolumn.n
    cov.append(coverage)
    pos.append(position)



#fig = plt.figure()
#ax1 = fig.add_subplot(211)
#t = np.arange(0.01, 10.0, 0.01)
#s1 = cov #np.exp(t)
#s2 = pos
#ax1.plot(s2,s1, 'b')
#ax1.set_xlabel('pos (bp)')
# Make the y-axis label and tick labels match the line color.
#ax1.set_ylabel("Coverage (x reads)", color='b')

#x = s2
#y = s1

#ax2 = fig.add_subplot(212, axisbg='#FFFFCC')
#line2, = ax2.plot(x, y, '-')


#def onselect(xmin, xmax):
#    indmin, indmax = np.searchsorted(x, (xmin, xmax))
#    indmax = min(len(x)-1, indmax)
#
#    thisx = x[indmin:indmax]
#    thisy = y[indmin:indmax]
#    line2.set_data(thisx, thisy)
#    ax2.set_xlim(thisx[0], thisx[-1])
#    ax2.set_ylim(thisy.min(), thisy.max())
#    fig.canvas.draw()

# set useblit True on gtkagg for enhanced performance
#span = SpanSelector(ax1, onselect, 'horizontal', useblit=True,
#                    rectprops=dict(alpha=0.5, facecolor='red') )



#ax1.axvspan(62076,69141,facecolor='gray')#	3DXL6
#ax1.axvspan(71580,77407,facecolor='gray')#	2DS3
#ax1.axvspan(82174,87568,facecolor='gray')#	3DXS3
#ax1.axvspan(97731,107326,facecolor='gray')#	3DXL7
#ax1.axvspan(132747,140360,facecolor='gray')#	3DXL4
#ax1.axvspan(144211,150034,facecolor='gray')#	2DS2
#ax1.axvspan(154794,160963,facecolor='gray')#	3DXS2
#ax1.axvspan(170279,179882,facecolor='gray')#	3DXL5
#ax1.axvspan(205374,212910,facecolor='gray')#	3DXL2
#ax1.axvspan(214470,222555,facecolor='gray')#	2DS1
#ax1.axvspan(230427,242938,facecolor='gray')#	3DXL3
#ax1.axvspan(273824,279418,facecolor='gray')#	3DXS1
#ax1.axvspan(304526,312244,facecolor='gray')#	3DXL1
#ax1.axvspan(313914,323934,facecolor='gray')#	2DL1
#ax1.axvspan.set_colour('r')
#for tl in ax1.get_yticklabels():
#    tl.set_color('k')

    

#ax2 = ax1.twinx()


#s2 = genePositions #np.sin(2*np.pi*t)
#ax2.plot(s2, 'r|')
#ax2.set_ylabel('genes', color='r')
#for tl in ax2.get_yticklabels():
#    tl.set_color('r')

#upLine(x=100, linewidth=4, color='r')
#plt.show()


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(211, axisbg='#FFFFCC')

x = pos #np.arange(0.0, 5.0, 0.01)
y = cov #np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))

ax.plot(x, y, '-')
#ax.set_ylim(-2,2)
ax.set_title('Press left mouse button and drag to test')

ax2 = fig.add_subplot(212, axisbg='#FFFFCC')
line2, = ax2.plot(x, y, '-')


def onselect(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x)-1, indmax)

    thisx = x[indmin:indmax]
    thisy = y[indmin:indmax]
    line2.set_data(thisx, thisy)
    ax2.set_xlim(thisx[0], thisx[-1])
    thisymax = max(thisy)
    ax2.set_ylim(0, thisymax)
    fig.canvas.draw()

# set useblit True on gtkagg for enhanced performance
span = SpanSelector(ax, onselect, 'horizontal', useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red') )



ax.axvspan(62076,69141,facecolor='gray')#	3DXL6
ax.axvspan(71580,77407,facecolor='gray')#	2DS3
ax.axvspan(82174,87568,facecolor='gray')#	3DXS3
ax.axvspan(97731,107326,facecolor='gray')#	3DXL7
ax.axvspan(132747,140360,facecolor='gray')#	3DXL4
ax.axvspan(144211,150034,facecolor='gray')#	2DS2
ax.axvspan(154794,160963,facecolor='gray')#	3DXS2
ax.axvspan(170279,179882,facecolor='gray')#	3DXL5
ax.axvspan(205374,212910,facecolor='gray')#	3DXL2
ax.axvspan(214470,222555,facecolor='gray')#	2DS1
ax.axvspan(230427,242938,facecolor='gray')#	3DXL3
ax.axvspan(273824,279418,facecolor='gray')#	3DXS1
ax.axvspan(304526,312244,facecolor='gray')#	3DXL1
ax.axvspan(313914,323934,facecolor='gray')#	2DL1



plt.show()










