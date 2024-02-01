#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Split the line into link and link count
    link, count = line.strip().split('\t')
    count = int(count)
    print(f"{link}\t{count}")
