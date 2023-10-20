#!/usr/bin/env python3

import re

my_file=open ("Python_07_ApoI.fasta","r")
for line in my_file:
	line=line.rstrip()
	found=re.search(r".AATT.",line)

	print(found)

#fasta file insert ^ at cut site

	sub=re.sub(r"(.AATT.)", r"^\1" ,line)
  #sub.group(1)
	print(sub)
	
	#convert into cut sites annotated

	x=sub.split("^")
	print(x)

	y=sorted(x,key=len)
	
	print(y)

