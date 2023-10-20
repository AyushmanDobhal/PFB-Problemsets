#!/usr/bin/env python3

import re

my_file = open("Python_07_nobody.txt","r")

line=0
for line in my_file:
 substituted=(re.sub(r"Nobody" , "Michael",line))
 if substituted==None:
  continue
 print(substituted)

