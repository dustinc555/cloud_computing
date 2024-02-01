#!/usr/bin/env python3
import sys
import json
import re

# Read stopwords and delimiters from files
with open(sys.argv[1], 'r') as stopWordsFile:
    stopWords = set(stopWordsFile.read().splitlines())

with open(sys.argv[2], 'r') as delimitersFile:
    # Directly split the delimiters string into a list
    delimiters = list(delimitersFile.read().strip())

for line in sys.stdin:
    # Parse the JSON line
    data = json.loads(line)

    # Extract relevant information
    business_id = data['business_id']
    stars = data['stars']
    text = data['text']

    # Convert stars to the new range (1 to 5) -> (-2 to 2)
    stars = (stars - 3)

    # Tokenize and preprocess the review text
    tokens = re.split('[' + re.escape(''.join(delimiters)) + ']', text.lower())
    
    # Remove common words by filtering stopWords
    tokens = [token for token in tokens if token not in stopWords]

    # Emit business_id, stars, and length of tokens
    print(f"{business_id}\t{stars}\t{len(tokens)}")
