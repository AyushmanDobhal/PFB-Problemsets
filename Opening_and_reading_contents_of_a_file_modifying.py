#!/usr/bin/env python3
import re


My_file = open("Python_07_nobody.txt","r")

my_file = ""

for x in My_file:
 my_file = my_file + x

print(re.findall(r"Nobody",my_file))

