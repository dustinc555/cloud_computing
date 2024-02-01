#!/usr/bin/env python3
import sys

# Initialize variables for the top business IDs
top_businesses = []

for line in sys.stdin:
    # Split the line into business_id and weighted average
    business_id, weighted_average = line.strip().split('\t')
    weighted_average = float(weighted_average)

    # Add the business ID to the list
    top_businesses.append((business_id, weighted_average))

# Sort the list in descending order based on weighted average and get the top 10
sorted_top_businesses = sorted(top_businesses, key=lambda x: x[1], reverse=True)[:10]

# Output the results
for business_id, weighted_average in sorted_top_businesses:
    print(f"{business_id}")