#!/usr/bin/env python3

import re
import sys

file=sys.argv[1]


with open(r"file", "r") as file:

	found=re.search(r"(Nobody)" ,Python_07_nobody.txt)
	print("Found using re")
