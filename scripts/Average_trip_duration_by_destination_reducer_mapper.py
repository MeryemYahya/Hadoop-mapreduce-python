#!/usr/bin/env python3

import sys
import datetime

header = next(sys.stdin)
header = header.strip().split(",")

for line in sys.stdin.readlines():
    line = line.strip().split(",")
    try:
        date1 = line[header.index('tpep_pickup_datetime')]
        date2 = line[header.index('tpep_dropoff_datetime')]
    except ValueError:
        date1 = line[header.index('lpep_pickup_datetime')]
        date2 = line[header.index('lpep_dropoff_datetime')]

    date1 = datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(line[2], "%Y-%m-%d %H:%M:%S")
    duration = date2 - date1
    dest = line[header.index('DOLocationID')]
    print(dest, duration.total_seconds())
