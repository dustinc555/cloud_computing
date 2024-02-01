#!/usr/bin/env python3
import sys

# Read the league IDs from the file
with open(sys.argv[1], 'r') as league_file:
    league_set = set(line.strip() for line in league_file)

for line in sys.stdin:
    # Split the line into page ID and link count
    page_id, count = line.strip().split('\t')
    count = int(count)

    # Emit the page ID with its popularity count if it's in the league
    if page_id in league_set:
        print(f"{page_id}\t{count}")
