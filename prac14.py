#using python NLTK, perform the following Natural language processing(NLP) taks for text content
#atokenizing
#bfiltering stop words
#cstemming

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

text = input("Enter text: ")

tokens = word_tokenize(text)
filtered = [w for w in tokens if w.lower() not in stopwords.words('english')]
stemmed = [PorterStemmer().stem(w) for w in filtered]

print("Tokens: ",tokens)
print("filtered: ",filtered)
print("Stemmed: ", stemmed) 