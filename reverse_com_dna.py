#!/usr/bin/env python3
import sys

dna = sys.argv[1]


dna_comp=dna.replace("A","t").replace("C","g").replace("G","c").replace("T","a")

print(f"Complement is 3' {dna_comp.upper()} 5'")


dna_comp2=dna_comp.upper()

Reverse_complement=dna_comp2[::-1]

print(f"Reverse complement is 5' {Reverse_complement} 3'")
