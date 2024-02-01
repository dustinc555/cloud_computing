#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Split the line into page ID and links
    parts = line.strip().split(':')
    if len(parts) == 2:
        page_id = int(parts[0].strip())
        links = parts[1].strip().split()

        # Emit links no value required just add one per event
        for link in links:
            print(f"{link}")
