#!/usr/bin/env python3
import sys

tokens = {}

for line in sys.stdin:
    token = line.strip()

    if token not in tokens:
        tokens[token] = 0
    tokens[token] += 1
    
for current_token in tokens.keys():
    current_count = tokens[current_token]
    print(f"{current_token}\t{current_count}")
