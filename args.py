#!/usr/bin/env python
import sys

if len(sys.argv) != 5:
    sys.exit('Sorry, but you seem not to have the correct number of arguments.')
if (int(sys.argv[2]) % 2) != 0:
    sys.exit('Page Size must be a number divisible by 2 number.')
if (sys.argv[3] is ('clock' and 'lru' and 'fifo')):
    sys.exit('Argument 3 must be either: clock, lru, or fifo')
if ((int(sys.argv[4]) != 0) and (int(sys.argv[4]) != 1)):
    sys.exit('Argument 4 must be either: 1 or 0')