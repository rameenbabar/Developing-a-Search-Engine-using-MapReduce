#!/usr/bin/env python

import sys

current_word = None
current_doc_ids = set()
word_count = 0

# Read input from stdin
for line in sys.stdin:
    # Split the line into word_id and count
    word_id, doc_id = line.strip().split('\t')
    
    # Convert word_id to integer
    word_id = int(word_id)
    
    # If the word_id changes, it means we're moving to the next word
    if current_word != word_id:
        # If this isn't the first word, print the count of documents for the previous word
        if current_word is not None:
            print(f'{current_word}\t{len(current_doc_ids)}')
        
        # Reset variables for the new word
        current_word = word_id
        current_doc_ids = set()
    
    # Add the document ID to the set for the current word
    current_doc_ids.add(doc_id)

# Print the count for the last word
if current_word is not None:
    print(f'{current_word}\t{len(current_doc_ids)}')

