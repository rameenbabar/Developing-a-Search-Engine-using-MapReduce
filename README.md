# Developing a Search Engine using MapReduce Technology

## Introduction:
The objective of this assignment was to implement a Search Engine using Hadoop’s MapReduce Framework. The problem of managing enormous volumes of data while preserving quick responses was first addressed by search engines. In less than a millisecond, a search engine provides a list of the most relevant information after quickly processing hundreds to thousands of queries every second. However, in the field of information retrieval, the difficulty of finding relevant information is a crucial problem which basically involves **indexing of documents** and **processing queries**. Hadoop's MapReduce technology provides a practical approach for indexing large text corpora that are larger than what can fit on a single machine.

## Implementation:
### **Information Retrieval:**
Extracting textual data is the most basic task in information retrieval. When a query is submitted to the search engine, its task is to determines which of the documents in its collection are most relevant to a user's query. The TF/IDF Vector Space model is among the most basic information retrieval models and we utilized it to achieve this.

### **Vector Space model:**

**•	Preprocessing:**

Before starting the implementation of the vector space model, we performed preprocessing on the provided dataset to ensure that the text was in a consistent format. This involved conversion to lowercase, removal of any special characters and white spaces and most importantly word tokenization and removing stopwords using the **nltk library**.

**•	Vocabulary:**

The first step of the vector space model was to create a vocabulary which was basically a dictionary containing all the unique terms found in the corpus, ensuring that the vocabulary had no duplicates. The unique terms were extracted from the **SECTION_TEXT** column from our dataset. Each word/term in the vocabulary was assigned a unique ID so that accessing these terms in the upcoming tasks was easy.

**•	Term Frequency-TF:**

After creating the vocabulary, we had to calculate the term frequency which is basically the number of times a term(word) appears in a specific section text, in our case. Again, we utilized a dictionary for the term frequencies. A loop was used to iterate over the **SECTION_TEXT** column and it incremented the count of each term every time it was encountered. It is printed for each section text in the following format **(Unique ID, Frequency)** where unique id is the ID which was assigned in the vocabulary and frequency is the count.

**•	Inverse Document Frequency-IDF:**

The IDF reflects the number of documents in which a specific term appears. A high IDF means that the term is not distinctive in the section texts. To calculate the IDF we initialized an empty dictionary to store document frequency of each term. A loop was utilized to iterate over the vocabulary and another loop was used to iterate over the **SECTION_TEXT** column and it incremented the document (section text) frequency count each time that term appeared in it.

**•	Calculating TF/IDF Weights:**

The TF/IDF weights are calculated by dividing the term frequency with the inverse document frequency. For each section text, a dictionary called **term_frequency** is created to store the frequency of each term. It then iterates through each term in the **SECTION_TEXT** and update its frequency in the **term_frequency** dictionary. For each word, it calculates its weight by dividing its frequency by its document frequency and then prints the weights for each section along with the index of the word and its weight.

**•	Query Vector:**

We start with creating a vector for each section text **(section_weights)**, numerical representation (vector) for each section text, where each dimension of the vector corresponds to a term in the vocabulary, and the value of each dimension represents the TF/IDF weight of that term in the section text. Terms that exist in the section text are assigned with their respective weights and the rest of the values in the vector remain zero.

The query vector is created when the user enters a query, processes a user-input query sentence and computes a vector for all the section texts. It calculates the average weight of each word in the query sentence across all section texts and then updates the corresponding index in the **query_list** with the average weight.

**•	Calculating the Relevance Score:**

The relevance of a **section_text** to the query is calculated by the inner product **(scalar product)** of the two vectors, the **section_weights** vector and the **query_list** vector. The **word_relevance_score** is list consisting of relevance scores of each term which are basically the term’s TF/IDF weights. To compute the relevance score for each section text with respect to the query we receive as input from the user, it multiplies (inner product) the **section_weights[query_word_index]** with the **word_relevance_score** and then adds this calculated relevance score for the term to the **section_total_relevance_score** to provide the relevance score for the entire query sentence.

## Conclusion:

This implementation aims to solve the problem of finding relevant information during information retrieval. By computing relevance scores for each section, we are able to determine how closely each section is related to the query. This identification is based on the similarity between the content of each section and the query sentence. Sections that contain words similar to those in the query sentence are likely to receive higher relevance scores. Search engines can use these relevance scores to present search results in a ranked order, prioritizing sections that are likely to be most useful to the user.

In summary, this approach enables the identification and ranking of sections based on their relevance to a query, facilitating efficient information retrieval and decision-making processes. It helps users or systems prioritize and focus on sections that are most likely to contain the information they are seeking.






