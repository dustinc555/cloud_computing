#!/usr/bin/env python3
import sys

# Initialize variables for the top links
top_links = []

# Read the input and add links and counts to the list
for line in sys.stdin:
    link, count = line.strip().split('\t')
    count = int(count)
    top_links.append((link, count))

# Sort the list in descending order based on counts and get the top 10
sorted_top_links = sorted(top_links, key=lambda x: x[1], reverse=True)[:10]

# Output the results
for link, count in reversed(sorted_top_links):
    print(f"{link}\t{count}")