#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Split the line into business_id and weighted average
    business_id, weighted_average = line.strip().split('\t')
    weighted_average = float(weighted_average)

    # Emit the weighted average as the key with the business_id
    print(f"{business_id}\t{weighted_average}")
