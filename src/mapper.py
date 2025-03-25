#!/usr/bin/env python

import sys
import re
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load NLTK stopwords
stop_words = set(stopwords.words('english'))

#preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.strip() and token not in stop_words]
    return tokens


word_index = {}  # Dictionary to store unique words and their index
doc_term_freq = {}  # Dictionary to store term frequencies per document
doc_count = 0   # Counter to keep track of the number of documents processed


with sys.stdin as csvfile:  # Read data from CSV file
    reader = csv.reader(csvfile)
    for row in reader:
        #the first column is article_id and the second column is section_text
        if len(row) >= 2:
            article_id, section_text = row[0], row[1]
            # Preprocess the text
            tokens = preprocess_text(section_text)
            # Increment document counter
            doc_count += 1
            # Initialize term frequency counter for the current document
            doc_term_freq[article_id] = {}
            # Update word_index and term frequencies for the current document
            for token in tokens:
                if token not in word_index:
                    word_index[token] = len(word_index)  # Assign a unique index to the word
                # Increment term frequency for the current word in the current document
                word_id = word_index[token]
                doc_term_freq[article_id][word_id] = doc_term_freq[article_id].get(word_id, 0) + 1
            # If the first document has been processed, break the loop
            if doc_count >= 1:
                break
        else:
            print("Error: Input line does not have expected format.")

# Print term frequencies for the first document
first_doc_id = next(iter(doc_term_freq))
#print(f'Term frequencies for document ID: {first_doc_id}')
for word_id, count in doc_term_freq[first_doc_id].items():
    print(f'{word_id}\t{count}')

