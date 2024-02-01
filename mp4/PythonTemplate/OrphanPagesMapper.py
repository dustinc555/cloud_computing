#!/usr/bin/env python3
import sys

try:

    for line in sys.stdin:
        # Split the line into page ID and links
        parts = line.strip().split(":")
        if len(parts) == 2:
            page_id = int(parts[0].strip())
            links = parts[1].strip().split()

            # Emit the page ID as the key with a flag indicating it's linking to
            print(f"{page_id}\tlinking")

            # Emit links as the key with a flag indicating it's being linked to
            for link in links:
                # If the link is a link to itself that does not make it not an orphan page
                if int(link) != page_id:
                    print(f"{link}\tlinked")

except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
