#!/usr/bin/env python3
import sys
dna = sys.argv[1]

#calculating AT content of a sequence


total=len(dna)
A_count=dna.count("A")
T_count=dna.count("T")


AT_content=(A_count+T_count)/(total)

print(total)
print(A_count)
print(T_count)
print(AT_content)
