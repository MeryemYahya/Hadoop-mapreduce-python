#!/usr/bin/env python3

import datetime
import sys


dests = {}
current_dest = None
duration_count = 0
dest = None

# Read taxi zone lookup file and create dictionary with id and name zone
dictionary = {}
file = open("./taxi+_zone_lookup.csv")
for line in file:
    line = line.strip().split(',')
    dictionary[line[0]] = line[2]


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().split(' ', 1)
    # parse the input we got from mapper.py
    dest = line[0]
    duration = line[-1]

    # convert duration (currently a string) to int
    try:
        duration = float(duration)

    except ValueError:
        # duration was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: payment) before it is passed to the reducer
    if current_dest == dest:
        duration_count += duration
        dests[current_dest] += 1
    else:
        if current_dest:
            # write result to STDOUT
            print(current_dest, dictionary[current_dest], str(
                datetime.timedelta(seconds=duration_count/dests[current_dest])))
        duration_count = duration
        current_dest = dest
        dests[dest] = 1

# do not forget to output the last dest if needed!
if current_dest == dest:
    print(current_dest, dictionary[current_dest], str(datetime.timedelta(
        seconds=duration_count/dests[current_dest])))
