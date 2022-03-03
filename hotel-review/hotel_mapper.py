#!/usr/bin/env python
"""hotel_mapper.py"""

import sys


for line in sys.stdin:
    line = line.strip().split(",")
    value=line[-1]
    print '%s\t%s' % (value, 1) 

