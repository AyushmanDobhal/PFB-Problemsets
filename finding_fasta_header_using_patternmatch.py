#!/usr/bin/env python3
import sys
import re


my_file=open (sys.argv[1],"r")

my_seqs={}


for line in my_file:
	line=line.rstrip()

#>gi|170746|gb|M12277.1|WHTH4091 Wheat histone H4 TH091 gene
	
	match=re.match(r">(\S+)\s+(.*)",line)
	if match:
		print("id:",match.groups()[0],"description:",match.groups()[1])
		seq_id=match.groups()[0]
		my_seqs[seq_id]=""
	else:
		#print("here 0")

		my_seqs[seq_id] += line 



print(my_seqs)


for seq_id in my_seqs:
	sequence=my_seqs[seq_id]
	#print(sequence)
	total=len(sequence)
	#print('here 1')

	A_count=dna.count("A")
	T_count=dna.count("T")
	a_count=dna.count("a")
	t_count=dna.count("t")
	G_count=dna.count("G")
	C_count=dna.count("C")
	g_count=dna.count("g")
	N_count=dna.count("N")
	#print("here 2")
	
	AT_content=(A_count+T_count)/(total)


	print(f'total is {total}','A_count is {A_count}', 'a_count is {a_count}', 'Ncount is {N_count}')

		

