#!/usr/bin/env python3

import sys
dna=sys.argv[1]

a_count=dna.count("A")
c_count=dna.count("C")
t_count=dna.count("T")
g_count=dna.count("G")

print(a_count,c_count,g_count,t_count)

