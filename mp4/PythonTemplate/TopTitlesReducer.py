#!/usr/bin/env python3
import sys

# Initialize variables for the top titles
top_titles = []

# Read the input and add tokens and counts to the list
for line in sys.stdin:
    token, count = line.strip().split('\t')
    count = int(count)
    top_titles.append((token, count))

# Sort the list in descending order based on counts and get the top 10
sorted_top_titles = reversed(sorted(top_titles, key=lambda x: x[1], reverse=True)[:10])

# Output the results
for token, count in sorted_top_titles:
    print(f"{token}\t{count}")
