#!/usr/bin/env python3
import sys

header = next(sys.stdin)
header = header.strip().split(",")

for line in sys.stdin.readlines():
    line = line.strip().split(",")
    value = line[header.index('payment_type')]
    print(value,1) 
