# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:28:31 2021

@author: Victoria Wingo

Datacamp unguided project Word Frequency in Classic Novels
Question: Of the 10 most-common words in Peter Pan, 
    which ones are character names?
"""

import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter

# Get File and Text
# Getting the Peter Pan HTML 
r = requests.get("https://www.gutenberg.org/files/16/16-h/16-h.htm")
# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'
# Extracting the HTML from the request object
html = r.text
# Printing the first 2000 characters in html
print(html[:2000])
# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, features="html.parser")
# Getting the text out of the soup
text = soup.get_text()
# Printing out text between characters 32000 and 34000
print(text[32000:34000])

# Tokenize 
# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
# Tokenizing the text
tokens = tokenizer.tokenize(text)
# Printing out the first 8 words / tokens 
print(tokens[:8])
# Create a list called words containing all tokens transformed to lower-case
words = [token.lower() for token in tokens]
# Printing out the first 8 words / tokens 
print(words[:8])

# Remove unimportant words
# Getting the English stop words from nltk
sw = nltk.corpus.stopwords.words('english')
# Printing out the first eight stop words
print(sw[:8])
# Create a list words_ns containing all words that are in words but not in sw
words_ns = [word for word in words if word not in sw]
# Printing the first 5 words_ns to check that stop words are gone
print(words_ns[:5])

# Count tokens
# Initialize a Counter object from our processed list of words
count = Counter(words_ns)
# Store 10 most common words and their counts as top_ten
top_ten = count.most_common(10)
# Print the top ten words and their counts
print(top_ten)

protagonists = ['Peter', 'Wendy', 'Hook', 'John']
