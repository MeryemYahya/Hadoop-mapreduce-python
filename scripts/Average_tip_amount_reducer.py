#!/usr/bin/env python3

import sys

counter_tipamount = 0
current_count = 0

for line in sys.stdin:

    line = line.strip()
    line = line.split(' ', 1)
    tipamount = line[0]
    count = line[-1]
    try:
        count = int(count)
    except ValueError:
        continue
    try:
        tipamount = float(tipamount)
    except ValueError:
        continue

    counter_tipamount += tipamount
    current_count += count

print("Average tip amount :", counter_tipamount/current_count)

