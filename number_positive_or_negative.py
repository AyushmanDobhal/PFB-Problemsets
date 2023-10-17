#!/usr/bin/env python3
import sys
#testing numbers if more or less than,zero,odd or even.
integer = int(sys.argv[1]) 

if integer > 0:
 print("positive_integer")
 if integer >50:
  print("integer more than 50")
  if integer % 2 == 0:
   print("integer is EVEN")
  else:
   print("integer is ODD")
if integer < 0:
 print("negative_integer")
  
if integer == 0:
 print( "must be 0")

