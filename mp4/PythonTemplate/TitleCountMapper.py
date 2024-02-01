#!/usr/bin/env python3
import sys
import re

# Load stop words and delimiters from files
stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath, 'r') as stopWordsFile:
    stopWords = set(stopWordsFile.read().splitlines())

with open(delimitersPath, 'r') as delimitersFile:
    # Directly split the delimiters string into a list
    delimiters = list(delimitersFile.read().strip())

for line in sys.stdin:
    # Tokenize the title
    tokens = re.split('[' + re.escape(''.join(delimiters)) + ']', line.strip())

    # Filter out stop words and output counts
    for token in tokens:
        if token.lower() not in stopWords and token:
            print(f"{token.lower()}")
