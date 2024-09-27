#!/usr/bin/env python3

import sys


years = {}
current_year = None
distance_count = 0
year = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    line = line.split(' ', 1)
    distance = line[-1]
    year = line[0]

    # convert distance (currently a string) to int
    try:
        distance = float(distance)

    except ValueError:
        # distance was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: year) before it is passed to the reducer
    if current_year == year:
        distance_count += distance
        years[current_year] += 1
    else:
        if current_year:
            # write result to STDOUT
            if years[current_year] == 0:
                avg = 0
            else:
                avg = distance_count/years[current_year]
            print(current_year, avg, "mi")
        distance_count = distance
        current_year = year
        years[year] = 1

# do not forget to output the last year if needed!
if current_year == year:
    years[current_year] += 1
    if years[current_year] == 0:
        avg = 0
    else:
        avg = distance_count/years[current_year]
    print(current_year, avg, "mi")
