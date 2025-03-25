# Developing a Search Engine using MapReduce Technology

## Overview:
This project implements a basic search engine using the **MapReduce paradigm** on a subset of the English Wikipedia dataset. It demonstrates core concepts in **Information Retrieval**, including **TF-IDF**, **Vector Space Models**, and distributed computing using **Apache Hadoop**.

The problem of managing enormous volumes of data while preserving quick responses was first addressed by search engines. In less than a millisecond, a search engine provides a list of the most relevant information after quickly processing hundreds to thousands of queries every second. However, in the field of information retrieval, the difficulty of finding relevant information is a crucial problem which basically involves **indexing of documents** and **processing queries**. Hadoop's MapReduce technology provides a practical approach for indexing large text corpora that are larger than what can fit on a single machine.


## Dataset

We used a subset of the English Wikipedia dump, formatted as a CSV with the following fields:

- `ARTICLE_ID`: Unique identifier for each Wikipedia article.
- `TITLE`: Title of the article.
- `SECTION_TITLE`: Title of each subsection.
- `SECTION_TEXT`: Main text content from each subsection.

[Download the dataset](https://en.wikipedia.org/wiki/Wikipedia:Database_download)

## Objective

Build a naive search engine that:
1. **Indexes** a large corpus using MapReduce.
2. Calculates **TF**, **IDF**, and **TF-IDF** scores.
3. Uses a **Vector Space Model** to evaluate document-query relevance.
4. Outputs the **most relevant documents** for a given query.

## Technologies Used

- **Apache Hadoop** – Distributed processing with MapReduce.
- **NLTK** – Tokenization, stopword removal, preprocessing.
- **Python** – Core logic and MapReduce scripting.
- **Jupyter Notebooks** – Preprocessing and local testing.

## Workflow Overview

### 1. **Preprocessing**

Performed via `preprocessing.ipynb` and `search_engine.ipynb`:
- Clean and normalize the text.
- Tokenize using `nltk.word_tokenize`.
- Remove stopwords and punctuation.
- Build a vocabulary of unique words.

### 2. **TF / IDF / TF-IDF Calculation**

- **TF**: Term frequency of each word per document.
- **IDF**: Number of documents a word appears in.
- **TF-IDF**: `TF / DF` weighting scheme to build sparse document vectors.

All intermediate data (TF, IDF, TF-IDF weights) are stored in the `output/` folder.

### 3. **Search Query**

- Query is preprocessed similarly.
- A vector is created for the query.
- Dot product between query vector and document vectors is calculated.
- Documents are ranked based on relevance score.

Output:
- `vocab.txt`:	Vocabulary list with each unique word and its assigned index.
- `tf.txt`:	**Term Frequencies (TF)**: Count of each term in every section/document.
- `idf.txt`:	**Inverse Document Frequencies (IDF)**: Number of documents each term appears in.
- `tfidf.txt`: **TF-IDF weights for each document:** TF divided by document frequency (DF).
- `query_list.txt`: The vector for the query.
- `relevance.txt`: Ranked documents with relevance scores and text.

## Using Hadoop MapReduce

### Mapper: `src/mapper.py`

- Reads CSV input (article ID, section text).
- Preprocesses text and computes word frequencies.
- Emits `(word_id, doc_id)` pairs.

### Reducer: `src/reducer.py`

- Aggregates document frequencies for each word.
- Outputs `(word_id, document_count)` – useful for IDF.

### Run the Job

```bash
# Run Hadoop MapReduce job
hadoop jar /path/to/hadoop-streaming.jar \
  -input /input/path/in/hdfs \
  -output /output/path/in/hdfs \
  -mapper "python3 src/mapper.py" \
  -reducer "python3 src/reducer.py" \
  -file src/mapper.py \
  -file src/reducer.py
```

## Deployment Notes
Ideal for distributed execution using a local or cloud-based Hadoop cluster (e.g., Azure, AWS EMR).

Dataset is large; for local development, test with a truncated CSV.
