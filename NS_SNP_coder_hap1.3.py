#!/usr/bin/env python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
import os
import gzip
import string
from Bio.Alphabet import generic_dna
import math


targetTXT = open(sys.argv[1], 'r')


records = list(SeqIO.parse(targetTXT, "fasta"))
record_dict = SeqIO.to_dict(SeqIO.parse(targetTXT, "fasta"))

standardbases = set()
standardbases.add('A')
standardbases.add('T')
standardbases.add('G')
standardbases.add('C')


def replaceIUB(IUB,REF):
	if IUB == "M":
		if REF == "A":
			return "C"
		else:
			return "A"	
	if IUB == "K":
		if REF == "G":
			return "T"
		else:
			return "G"
	if IUB == "S":
		if REF == "G":
			return "C"
		else:
			return "G"
	if IUB == "W":
		if REF == "A":
			return "T"
		else:
			return "A"
	if IUB == "Y":
		if REF == "T":
			return "C"
		else:
			return "T"
	if IUB == "R":
		if REF == "A":
			return "G"
		else:
			return "A"
	if IUB in standardbases:
		return IUB								



#SNP_gDNA_pos = 2640
#altBase = "C"
def __which_region__(gSNPpos):
	BEDFILE1 = open(sys.argv[2], 'r')
	for line in BEDFILE1:
		l1 = line.split("\t")
		startgeneSTR = l1[1]
		stopgeneSTR = l1[2]
		startgene = int(startgeneSTR)
		stopgene = int(stopgeneSTR)
		if gSNPpos > startgene:
			if gSNPpos < stopgene:
				return startgene
	pass

	

######## code to findout intron sizes, CDS pos, RES number, codon pos ##

def __CDS_pos__(SNP_gDNA_pos, seqID):
	genomicSNP = int(SNP_gDNA_pos)
	BEDFILE = open(sys.argv[2], 'r')
	seq1t = records[0]
	sequence = []
	introns = []
	intronStart = 0
	exonStart = 0
	SNP_CDS_pos = 0
	feature = "unknown - something wrong with this positon"
	for line in BEDFILE:
		l1 = line.split("\t")
		BedChrom = l1[0]
		startSTR = l1[1]
		stopSTR = l1[2]
		featureLine = l1[3]
		###### exon start - stop
		exon_line_start = l1[6]
		exon_line_stop = l1[7]
		exStartInt = int(exon_line_start)
		exStopInt = int(exon_line_stop)
		startEx = exStartInt - 1
		stopEx = exStopInt #- 1
		startINT = int(startSTR)
		stopINT = int(stopSTR)

		startofgene = __which_region__(genomicSNP)
		
		if startINT == startofgene:
			start = startINT - 1
			stop = stopINT #- 1
			sequence_line = seq1t.seq[startEx:stopEx] ##### break this up into two functions 1 to find the right range and 	the other to vreate the sequence
			seqSTR = str(sequence_line)
			sequence.append(seqSTR)
			intronINT = (startEx - (startofgene-1)) - intronStart
			intronStart = (stopEx - (startofgene-1))
			introns.append(intronINT)
			intronSIZE = sum(introns)	
			if SNP_gDNA_pos > startEx:
				if SNP_gDNA_pos < stopEx:
					SNP_CDS_pos = (SNP_gDNA_pos - (startofgene-1)) - intronSIZE
					feature = featureLine #.replace("\n","")
					#return SNP_CDS_pos
		pass
	pass
			
	resINTf = math.ceil(SNP_CDS_pos/3.0) - 1
	resNumberf = math.ceil(SNP_CDS_pos/3.0) - 1 
	resINT = int(resNumberf)
	resNumber = int(resINTf)
	resNumberSTR = str(resNumber)
	resINTstr = str(resNumber)

	codonMODULUS = (SNP_CDS_pos%3)


	if codonMODULUS == 0:
		codonPos = 3
	if codonMODULUS == 1:
		codonPos = 1
	if codonMODULUS == 2:
		codonPos = 2
	codonPosSTR = str(codonPos)

	SNP_CDS_posSTR = str(SNP_CDS_pos)
	#print "CDS pos = " + SNP_CDS_posSTR
	#print "Residue number = " + resNumberSTR
	#print "Codon pos = " + codonPosSTR


	CDS_seq = "".join(sequence)
	coding_dna = Seq(CDS_seq, generic_dna)
	protein = coding_dna.translate()
	proteinSTRING = str(protein)

	SNP_CDS_posINT = SNP_CDS_pos - 1

	#refBase = coding_dna[SNP_CDS_posINT]

	#proteinRES = coding_dna[SNP_CDS_posINT]
	#proteinRESstr = str(proteinRES)
	protenPOSistion = protein[resINT]
	protenPOSistionSTR = str(protenPOSistion) #### the protein influneced by the SNP position
	return BedChrom + "\t" + SNP_CDS_posSTR + "\t" + resNumberSTR + "\t" + codonPosSTR + "\t" + protenPOSistionSTR + "\t" + CDS_seq + "\t" + codonPosSTR + "\t" + resINTstr + "\t" + resNumberSTR + "\t" + feature + "\t" + proteinSTRING
	
def CodonUP(x, resINT2):
	codonLIST = []
	n = 0
	c = 3
	codonNumber = 1
	codonNumStr = str(codonNumber)
	length = len(x)
	while n < length:
		codon1 = x[n:n+3]
		n = n + c
		#codonNumber = codonNumber + 1
		#codonNumStr = str(codonNumber)
		codonLIST.append(codon1)
	#print codonLIST[142]
	return codonLIST[resINT2]

def altCodon(c,b,ab,p):
	if p == 1:
		return ab + c[1] + c[2]
	if p == 2:
		return c[0] + ab + c[2]
	if p == 3:
		return c[0] + c[1] + ab
	

def SNP_coder(CDS_Xdef_seq, refBase, altBase, codonPos, resNO):		
	REFcodon = CodonUP(CDS_Xdef_seq, resNO)
        #print REFcodon
        #print altBase
	ALTcodon = altCodon(REFcodon, refBase, altBase, codonPos)
	#print REFcodon
	#print ALTcodon

	REFcodonBIO = Seq(REFcodon, generic_dna)
	ALTcodonBIO = Seq(ALTcodon, generic_dna)

	REFprotein = REFcodonBIO.translate()
	ALTprotein = ALTcodonBIO.translate()

	RP = str(REFprotein)
	FP = str(ALTprotein)

	if FP != RP:
		return "N" + "\t" + REFcodon + "\t" + ALTcodon + "\t" + RP + "\t" + FP
	else:
		return "S" + "\t" + REFcodon + "\t" + ALTcodon + "\t" + RP + "\t" + FP


################## run through SNP file and call S/NS SNPs ##########
print "Chrom" + "\t" + "Position" + "\t" + "Ref" + "\t" + "Cons" + "\t" + "Reads1" + "\t" + "Reads2" + "\t" + "VarFreq" + "\t" + "Strands1" + "\t" + "Strands2" + "\t" + "Qual1" + "\t" + "Qual2" + "\t" + "Pvalue" + "\t" + "MapQual1" + "\t" + "MapQual2" + "\t" + "Reads1Plus" + "\t" + "Reads1Minus" + "\t" + "Reads2Plus" + "\t" + "Reads2Minus" + "\t" + "VarAllele" + "\t" + "chrom" + "\t" + "SNP_gDNA_pos" + "\t" + "SNP_CDS_pos" + "\t" + "SNP_Res_pos" + "\t" + "codon_pos" + "\t" + "Ref_RES" + "\t" + "Alt_RES" + "\t" + "S/NS" + "\t" + "feature"

#SNPfile = open(sys.argv[3], 'r')
SNPfile = sys.stdin
for line in SNPfile:
	lineList = line.split('\t')
	chrom = lineList[0]
	gSNP_pos = lineList[1]
	gSNP_posINT = int(gSNP_pos)
	REFb = lineList[2]
	gSNP_change = lineList[3]
	altREfb = lineList[-1].strip("\n").strip("\t").strip("").replace(" ","")#replaceIUB(gSNP_change, REFb)
	CDS_stats = __CDS_pos__(gSNP_posINT,chrom)
	CDS_statsLIST = CDS_stats.split('\t')
	#print __CDS_pos__(gSNP_posINT,'seq7')
	CDS_X_seq = CDS_statsLIST[5]
	codonPOSstr = CDS_statsLIST[6]
	residue_nostr = CDS_statsLIST[7]
	featureSTR = CDS_statsLIST[9]
	protseq = CDS_statsLIST[10]
	residue_no1 = int(residue_nostr)
	residue_no = residue_no1 #- 1
	codonPOSint = int(codonPOSstr)
	SNP_coder_stats = SNP_coder(CDS_X_seq, REFb, altREfb, codonPOSint, residue_no)
	SNP_coder_statsList = SNP_coder_stats.split('\t')
	proteinToShow = Seq(CDS_X_seq, generic_dna)
	proteinToShow1 = proteinToShow.translate()
	proteinNumberDisplayINT = int(CDS_statsLIST[2]) + 1 ### changed after realising it was 1 too low(16/11/2012)
	proteinNumberDisplaystr = str(proteinNumberDisplayINT)
		 
	print line.replace("\n", "") + "\t" + CDS_statsLIST[0] + "\t" + gSNP_pos + "\t" + CDS_statsLIST[1] + "\t" + proteinNumberDisplaystr + "\t" + CDS_statsLIST[3] + "\t" + SNP_coder_statsList[3] + "\t" + SNP_coder_statsList[4] + "\t" + SNP_coder_statsList[0] + "\t" + featureSTR + "\t" + protseq # + "\t" + proteinToShow 
pass









