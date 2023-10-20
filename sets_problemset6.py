#!/usr/bin/env python3
import sys

set1=sys.argv[1]
set2=sys.argv[2]



#spliting sets at,
setA=set(set1.split(","))
setB=set(set2.split(","))


#printing set list
print(f" A is {setA},B is{setB}")

#diffrence b/w two sets
difference=setA.difference(setB)

print(f" difference between sets is {difference}")

union_of_two_sets=setA.union(setB)


print(f" union_of_two_sets is {union_of_two_sets}")




