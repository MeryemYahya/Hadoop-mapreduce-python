#!/usr/bin/env python3

import sys
import datetime

header = next(sys.stdin)
header = header.strip().split(",")


for line in sys.stdin.readlines():
    line = line.strip().split(",")
    date = line[2]
    try:
        date = line[header.index('tpep_dropoff_datetime')]
    except ValueError:
        date = line[header.index('lpep_dropoff_datetime')]

    year = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").year
    distance = line[header.index('trip_distance')]
    print(year, distance)
