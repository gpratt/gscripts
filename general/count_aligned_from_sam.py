"""

Given a sam file counts chromosome frequencies 

"""

import argparse
from collections import Counter
import sys

parser = argparse.ArgumentParser(description='Counts Counts Chromosomes in sam file (used generally for getting counts of rRNA elements after filtering them), writes results to stdout')
parser.add_argument('--input', help='input sam file', default=sys.stdin)

args = parser.parse_args()
counts = Counter()

if args.input != sys.stdin:
    handle = open(args.input)
else:
    handle = args.input

for line in handle:
    line = line.strip().split()

    if line[0].startswith("@") or line[2] == "*":
        continue
    

    counts[line[2]] += 1

for name, count in counts.most_common():
    print name, count

