#!/usr/bin/env python3
import sys

# Initialize variables to store page popularity and league ranks
page_popularity = {}
league_ranks = {}

for line in sys.stdin:
    # Split the line into page ID and popularity count
    page_id, count = line.strip().split('\t')
    page_id, count = int(page_id), int(count)

    # Store the popularity count for each page
    page_popularity[page_id] = count

    # Initialize the rank for each page in the league
    if page_id not in league_ranks:
        league_ranks[page_id] = 0

# Calculate the rank for each page in the league
for page_id in league_ranks.keys():
    for other_page_id, other_count in page_popularity.items():
        if other_count < page_popularity[page_id]:
            league_ranks[page_id] += 1

# Output the results for pages in the league
for page_id in reversed(sorted(league_ranks.keys())):
    print(f"{page_id}\t{league_ranks[page_id]}")
