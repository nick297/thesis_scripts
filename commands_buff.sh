#!/bin/bash



echo $1


echo "Name" "\t" "total matches" "\t" "positions compared" "\t" "Percentage score"

echo "3DXL3 vs 3DXL5"
python NS_redvar2.py csv/group3_3DXL33DXL5.csv pileup/buffalo/buffalo_seq9.pileup 0 | python output/NS_redvar_out_cons2.py $1 01

echo "3DXL3 vs 3DXL7"
python NS_redvar2.py csv/group3_3DXL33DXL7.csv pileup/buffalo/buffalo_seq9.pileup 0 | python output/NS_redvar_out_cons2.py $1 01


echo "3DXL5 vs 3DXL3"
python NS_redvar2.py csv/group3_3DXL33DXL5.csv pileup/buffalo/buffalo_seq11.pileup 2 | python output/NS_redvar_out_cons2.py $1 23

echo "3DXL5 vs 3DXL7"
python NS_redvar2.py csv/group3_3DXL53DXL7.csv pileup/buffalo/buffalo_seq11.pileup 0 | python output/NS_redvar_out_cons2.py $1 01


echo "3DXL7 vs 3DXL3"
python NS_redvar2.py csv/group3_3DXL33DXL7.csv pileup/buffalo/buffalo_seq13.pileup 2 | python output/NS_redvar_out_cons2.py $1 2

echo "3DXL7 vs 3DXL5"
python NS_redvar2.py csv/group3_3DXL53DXL7.csv pileup/buffalo/buffalo_seq13.pileup 2 | python output/NS_redvar_out_cons2.py $1 2


######### group 2


echo "3DXL2 vs 3DXL4"
python NS_redvar2.py csv/group2_3DXL23DXL4.csv pileup/buffalo/buffalo_seq8.pileup 0 | python output/NS_redvar_out_cons2.py $1 01

echo "3DXL2 vs 3DXL6"
python NS_redvar2.py csv/group2_3DXL23DXL6.csv pileup/buffalo/buffalo_seq8.pileup 0 | python output/NS_redvar_out_cons2.py $1 01


echo "3DXL4 vs 3DXL2"
python NS_redvar2.py csv/group2_3DXL23DXL4.csv pileup/buffalo/buffalo_seq10.pileup 2 | python output/NS_redvar_out_cons2.py $1 23

echo "3DXL4 vs 3DXL6"
python NS_redvar2.py csv/group2_3DXL43DXL6.csv pileup/buffalo/buffalo_seq10.pileup 0 | python output/NS_redvar_out_cons2.py $1 01


echo "3DXL6 vs 3DXL2"
python NS_redvar2.py csv/group2_3DXL23DXL6.csv pileup/buffalo/buffalo_seq8.pileup 2 | python output/NS_redvar_out_cons2.py $1 2

echo "3DXL2 vs 3DXL4"
python NS_redvar2.py csv/group2_3DXL43DXL6.csv pileup/buffalo/buffalo_seq10.pileup 2 | python output/NS_redvar_out_cons2.py $1 2



##### group 3DL

echo "2DS1 vs 2DS2"
python NS_redvar2.py csv/group3DL_2DS1_2DS2.csv pileup/buffalo/buffalo_seq2.pileup 0 | python output/NS_redvar_out_cons2.py $1 01

echo "2DS1 vs 2DS3"
python NS_redvar2.py csv/group3DL_2DS1_2DS3.csv pileup/buffalo/buffalo_seq2.pileup 0 | python output/NS_redvar_out_cons2.py $1 01

echo "2DS2 vs 2DS1"
python NS_redvar2.py csv/group3DL_2DS1_2DS2.csv pileup/buffalo/buffalo_seq3.pileup 2 | python output/NS_redvar_out_cons2.py $1 23
#echo "no data"
echo "2DS2 vs 2DS3"
python NS_redvar2.py csv/group3DL_2DS2_2DS3.csv pileup/buffalo/buffalo_seq3.pileup 0 | python output/NS_redvar_out_cons2.py $1 01
#echo "no data"

echo "2DS3 vs 2DS1"
python NS_redvar2.py csv/group3DL_2DS1_2DS3.csv pileup/buffalo/buffalo_seq4.pileup 2 | python output/NS_redvar_out_cons2.py $1 2


echo "2DS3 vs 2DS2"
python NS_redvar2.py csv/group3DL_2DS2_2DS3.csv pileup/buffalo/buffalo_seq4.pileup 2 | python output/NS_redvar_out_cons2.py $1 2


##### group 4

echo "3DXS2 vs 3DXS3"
python NS_redvar2.py csv/group4.csv pileup/buffalo/buffalo_seq15.pileup 0 | python output/NS_redvar_out_cons2.py $1 01

echo "3DXS3 vs 3DXS2"
python NS_redvar2.py csv/group4.csv pileup/buffalo/buffalo_seq16.pileup 2 | python output/NS_redvar_out_cons2.py $1 2


#### group 1

echo "3DXL1 vs 3DSX1"
python NS_redvar2.py csv/group1.csv pileup/buffalo/buffalo_seq7.pileup 0 | python output/NS_redvar_out_cons2.py $1 0

echo "3DXS1 vs 3DLX1"
python NS_redvar2.py csv/group1.csv pileup/buffalo/buffalo_seq14.pileup 1 | python output/NS_redvar_out_cons2.py $1 1



