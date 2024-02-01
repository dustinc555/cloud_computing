#!/usr/bin/env python3
import sys

businesses = {}

for line in sys.stdin:
    # Split the line into business_id, stars, and length
    business_id, stars, length = line.strip().split('\t')
    stars, length = float(stars), int(length)

    if not business_id in businesses:
        businesses[business_id] = {'total_stars': 0, 'total_weight': 0}

    # Accumulate stars and length for the current business
    businesses[business_id]['total_stars'] += stars
    businesses[business_id]['total_weight'] += length

# Output the last business
for business_id in businesses.keys():
    business = businesses[business_id]
    total_stars = business['total_stars']
    total_weight = business['total_weight']
    weighted_average = total_stars / total_weight if total_weight > 0 else 0
    print(f"{business_id}\t{weighted_average}")
