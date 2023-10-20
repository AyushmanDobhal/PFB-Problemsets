#!/usr/bin/env python3
import re


my_file = open("Python_07_nobody.txt","r")

#my_file = ""

#for line  in My_file:
	
#	print(re.findall(r"Nobody",line))
#	print(line)

#my_match= re.finditer(r':Nobody',my_file)

#for found in my_match:
#	print(found.group(0))
#	print(found.start())
#	print(found.end())
#	print("\n")

#for found in re.finditer(r"Nobody", my_file):
line_number=0
for line in my_file:
	found=(re.search(r"Nobody", line))
	if found==None:
		continue
	whole = found.group(0)
	
	up_start = found.start(0)+1
	line_number+=1

	print(f"my match is {whole},on line {line_number},position{up_start}")


