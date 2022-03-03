#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_rate = None
current_count = 0
rate = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    rate, count = line.split('\t', 1)
    
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: rate) before it is passed to the reducer
    if current_rate == rate:
        current_count += count
    else:
        if current_rate:
            # write result to STDOUT
            print '%s\t%s' % (current_rate, current_count)
        current_count = count
        current_rate = rate

# do not forget to output the last rate if needed!
if current_rate == rate:
    print '%s\t%s' % (current_rate, current_count)