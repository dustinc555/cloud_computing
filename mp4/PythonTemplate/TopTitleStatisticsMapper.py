#!/usr/bin/env python3
import sys

for line in sys.stdin:
    token, count = line.strip().split('\t')
    print(f"{token}\t{count}")