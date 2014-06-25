#!/usr/bin/env python
import sys,operator
import os
import gzip
# usage: python extract_reads1e.py nameoffastqfile.fastq nameofnamesfile.txt > outfile.fastq


corrected   = gzip.open(sys.argv[2], "r")                       #list of sequence titles
uncorrected_fn = gzip.open(sys.argv[1], "r")            #target fastq file to pull sequences from
#output_fn      = "differences_fastq.ftq"                       #output file if used

corrected_names = set()                                         # Use a set instead of a list
for line in corrected:                                    # iterate through each line in list of seqs
    read_name = line.strip()                                      # each line assigned to variable read_line
    corrected_names.add(read_name)                              # Add read_line value to set (sort of a HASH)

#print 'done appending set, moving onto detection'


for line in uncorrected_fn:
    if line[0] == '@':
	l1 = line                                 # If line contains string from set
        l2 = uncorrected_fn.next()                       # Next line variable is assined the next line
        l3 = uncorrected_fn.next()                       # repeat for all of that sequence
        l4 = uncorrected_fn.next()                                   # Iterate through target fastq
        line1 = line.split(' ')
        line2 = str(line1[0])
	line3 = line2.strip(' ')
        if line3 in corrected_names:
            l1 = line                                 # If line contains string from set
            l2 = uncorrected_fn.next()                       # Next line variable is assined the next line
            l3 = uncorrected_fn.next()                       # repeat for all of that sequence
            l4 = uncorrected_fn.next()
        #l5 = uncorrected_fn.next()                       # Next line variable is assined the next line
        #l6 = uncorrected_fn.next()                       # repeat for all of that sequence
        #l7 = uncorrected_fn.next()
	#l8 = uncorrected_fn.next()
	    print l1.replace("\n", "")
	    print l2.replace("\n", "")
	    print '+'
	    print l4.replace("\n", "")



	#print line3
	#print line2
	#checkLine(line3, l1, l2, l4)
