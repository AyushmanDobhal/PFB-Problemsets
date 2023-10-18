#!/usr/bin/env python3
import sys
usernum = sys.argv[1]
count = int(usernum)


if count <40:
 message = "is less than 40"
 print(count,message)

elif count > 40:
 message = "more than 40"
 print(count,message)

else:

 message = "must be 40"
 print(count,message)
