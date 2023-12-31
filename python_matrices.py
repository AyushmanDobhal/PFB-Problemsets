#!/usr/bin/env python3
import sys
import re

# ssearch36 -q -S -s BP62 -m 8C rand5.fa q
# SSEARCH 36.3.8f May, 2017
# Query: random_5 consisting of 200 residues. - 200 aa
# Database: QFO_uniprot/ref
# Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score
# 7 hits found
#random_5	tr|D6WF18|D6WF18_TRICA	31.17	90	53	13	79	165	823	902	0.37	39.9
#random_5	sp|Q8GTS0|IP5P4_ARATH	50.00	38	16	6	11	48	3	34	1.8	35.7
#random_5	tr|D6WLD8|D6WLD8_TRICA	33.90	70	39	11	20	89	361	419	4.5	34.9
#random_5	tr|A7S0F9|A7S0F9_NEMVE	36.67	30	19	0	109	138	182	211	6.2	32.8
#random_5	sp|P38631|FKS1_YEAST	33.33	75	40	15	19	83	429	498	8.4	35.3
#random_5	tr|G3MXD6|G3MXD6_BOVIN	26.79	56	41	0	88	143	155	210	8.6	32.8
#random_5	tr|A7SX75|A7SX75_NEMVE	32.43	37	25	0	104	140	57	93	9	31.1
# SSEARCH processed 1 queries

my_file=open (sys.argv[1],"r")
my_file2= open (sys.argv[2],"r")


for line in my_file:
  
  line=line.rstrip()
  if "#" in line: 
   continue
  else:
   data=line.split('\t')
   #print(line)
   print (data[2],data[3],data[-2])

   break

