#!/usr/bin/env python3
import sys

try:

    is_linked_to = set()
    is_linking = set()

    for line in sys.stdin:
        # Split the line into key and value
        key, value = line.strip().split("\t")

        if value == "linked":
            # Mark this key as linked to
            is_linked_to.add(int(key))
        elif value == "linking":
            # Mark this key as linking to
            is_linking.add(int(key))

    # Find orphan pages (pages that link to nobody)
    orphan_pages = is_linking - is_linked_to

    # Print orphan page IDs
    for orphan_page in sorted(orphan_pages):
        print(orphan_page)
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")