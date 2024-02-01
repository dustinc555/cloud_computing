#!/usr/bin/env python3
import sys

links = {}

for line in sys.stdin:
    # For every link that is a additional 1 count
    link = int(line.strip())
    
    if not link in links:
        links[link] = 1
    else:
        links[link] += 1

# Output the link and the number of references it has
for page_id, count in links.items():
    print(f"{page_id}\t{count}")