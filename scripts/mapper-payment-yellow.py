#!/usr/bin/env python3


import sys
next(sys.stdin)
for line in sys.stdin.readlines():
    line = line.strip().split(",")
    value=line[9]
    print(value, 1) 
