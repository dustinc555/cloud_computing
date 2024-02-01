#!/usr/bin/env python3
import sys
import math

# Initialize variables for statistics calculation
total_count = 0
squared_sum = 0
min_count = float('inf')
max_count = float('-inf')

# Lists to store counts for variance calculation
counts = []

for line in sys.stdin:
    token, count = line.strip().split('\t')
    count = int(count)

    # Update statistics
    total_count += count
    squared_sum += count ** 2
    min_count = min(min_count, count)
    max_count = max(max_count, count)

    counts.append(count)

# Calculate mean, sum, minimum, maximum
mean = total_count // len(counts)
sum_counts = total_count
min_counts = min_count
max_counts = max_count

# Calculate variance
variance = sum((x - mean) ** 2 for x in counts) // len(counts)

# Output the results
print(f"Mean\t{mean}")
print(f"Sum\t{sum_counts}")
print(f"Min\t{min_counts}")
print(f"Max\t{max_counts}")
print(f"Var\t{variance}")
