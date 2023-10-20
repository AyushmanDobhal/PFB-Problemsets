#!/usr/bin/env python3

import re

my_file=open ("Python_07.fasta","r")

for line in my_file:
	line=line.rstrip()

#>gi|170746|gb|M12277.1|WHTH4091 Wheat histone H4 TH091 gene
	
	match=re.match(r">(\S+)\s+(.*)",line)
	if match:
		print("id:",match.groups()[0],"description:",match.groups()[1])
	else:
		pass

